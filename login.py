"""Script to force login/re-login, generate the Alexa cookie file, and send it to the API container."""

import logging
import sys
import asyncio
import os
from pathlib import Path
import pickle
import time
import requests # Needed for POSTing cookies
from typing import Optional, Dict # For cookie formatting type hint

# Selenium Imports
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

# Add src directory to path if running directly
# This helps Python find the alexa_shopping_list package (needed for config)
src_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), 'src')) # Point to ./src
if os.path.isdir(src_dir) and src_dir not in sys.path:
    sys.path.insert(0, src_dir)

try:
    # Only import config now
    from alexa_shopping_list.config import load_config, AppConfig
    # Removed: from alexa_shopping_list.auth import ensure_authentication
except ImportError as e:
    print(f"Error importing application modules: {e}", file=sys.stderr)
    print("Ensure the 'src' directory exists and you are running from the project root.", file=sys.stderr)
    sys.exit(1)

logger = logging.getLogger("login_script") # Renamed logger for clarity

# --- Helper Function (from auth.py) --- #
def format_selenium_cookies(selenium_cookies: list) -> Dict[str, str]:
    """Converts Selenium cookie list to a simple key-value dictionary."""
    return {cookie['name']: cookie['value'] for cookie in selenium_cookies}


async def main():
    """Main function to handle the login process."""
    try:
        # Config is loaded here
        config = load_config()
    except EnvironmentError as e:
        logging.basicConfig(level=logging.INFO) # Basic logging for error message
        logger.critical(f"Configuration error: {e}")
        sys.exit(1)

    # Setup logging based on config
    log_level = getattr(logging, config.log_level.upper(), logging.INFO)
    logging.basicConfig(
        level=log_level,
        format='%(asctime)s - %(name)s [%(levelname)s] %(message)s', # Added brackets to levelname
        stream=sys.stdout
    )
    if log_level > logging.DEBUG:
        # Suppress noisy library logs unless debugging
        logging.getLogger("urllib3").setLevel(logging.WARNING)
        logging.getLogger("selenium").setLevel(logging.INFO) # Keep selenium INFO for progress
        logging.getLogger("webdriver_manager").setLevel(logging.INFO)

    logger.info("Starting Alexa authentication process...")

    cookie_file = Path(config.cookie_path)

    # Check if cookie file exists and delete it to force re-auth
    if cookie_file.is_file():
        logger.info(f"Existing local cookie file found at '{config.cookie_path}'. Deleting to force re-authentication.")
        try:
            cookie_file.unlink()
        except OSError as e:
            logger.error(f"Error deleting existing cookie file '{config.cookie_path}': {e}")
            logger.warning("Proceeding with authentication attempt despite cookie deletion error.")

    # --- Start of merged ensure_authentication logic --- #
    logger.info("Starting browser login process.")
    logger.info("Setting up Selenium WebDriver...")

    driver = None
    login_and_upload_success = False # Changed variable name
    try:
        # --- Initialize WebDriver (using Chrome as default) ---
        options = webdriver.ChromeOptions()
        # options.add_argument("--headless")
        try:
            logger.debug("Initializing ChromeDriverManager...")
            service = ChromeService(ChromeDriverManager().install())
            logger.debug("Initializing webdriver.Chrome...")
            driver = webdriver.Chrome(service=service, options=options)
            logger.debug("WebDriver initialized.")
        except Exception as webdriver_err:
             logger.error("Failed to initialize Chrome WebDriver.", exc_info=True)
             logger.error("Ensure Google Chrome is installed and accessible.")
             print("\nPlease ensure Google Chrome is installed.", file=sys.stderr)
             sys.exit(1) # Exit directly if webdriver fails

        logger.info(f"Navigating to: {config.amazon_url}")
        driver.get(config.amazon_url)

        # --- User Interaction --- #
        print("-"*60)
        print("*** MANUAL LOGIN REQUIRED ***")
        print("A browser window should have opened.")
        print("Please log in to your Amazon account in that browser window.")
        print("Complete any 2FA or other verification steps displayed.")
        print("Once you are successfully logged in to the main Amazon page,")
        input("Press Enter in this console window to continue...")
        print("-"*60)

        # --- Extract, Save Locally, and POST Cookies --- #
        logger.info("Attempting to extract cookies from browser...")
        selenium_cookies = driver.get_cookies()

        if not selenium_cookies:
            logger.error("Failed to extract cookies from the browser after login.")
            logger.error("Please ensure you were fully logged in before pressing Enter.")
        else:
            logger.info(f"Successfully extracted {len(selenium_cookies)} cookies.")
            formatted_cookies = format_selenium_cookies(selenium_cookies)

            # Save the cookies locally (temporarily)
            try:
                with open(cookie_file, 'wb') as f:
                    pickle.dump(formatted_cookies, f)
                logger.info(f"Cookies temporarily saved locally to {config.cookie_path}")

                # *** Send cookies to the running API server ***
                api_cookie_endpoint = f"http://localhost:{config.api_port}/auth/cookies"
                logger.info(f"Attempting to send cookie file to API endpoint: {api_cookie_endpoint}")
                try:
                    with open(cookie_file, 'rb') as f_upload:
                        files = {'cookies_file': (cookie_file.name, f_upload, 'application/octet-stream')}
                        response = requests.post(api_cookie_endpoint, files=files, timeout=10)
                        response.raise_for_status() # Raise HTTPError for bad responses (4xx or 5xx)
                        logger.info(f"Successfully sent cookie file to API. Status: {response.status_code}")
                        login_and_upload_success = True # Set success flag HERE
                        # Optionally delete the local cookie file after successful upload
                        logger.info(f"Deleting temporary local cookie file: {cookie_file}")
                        try:
                            cookie_file.unlink(missing_ok=True)
                        except OSError as del_err:
                             logger.warning(f"Could not delete local cookie file {cookie_file}: {del_err}")

                except requests.exceptions.ConnectionError as conn_err:
                    logger.error(f"Could not connect to the API server at {api_cookie_endpoint}. Is it running?")
                    logger.error(f"Error: {conn_err}")
                except requests.exceptions.Timeout:
                    logger.error(f"Timeout while sending cookie file to {api_cookie_endpoint}.")
                except requests.exceptions.RequestException as req_err:
                    logger.error(f"Error sending cookie file to API: {req_err}")
                    if req_err.response is not None:
                        logger.error(f"API Response Status: {req_err.response.status_code}")
                        logger.error(f"API Response Body: {req_err.response.text}")
                except Exception as upload_err:
                    logger.error(f"Unexpected error during cookie file upload: {upload_err}", exc_info=True)

            except Exception as save_err:
                logger.error(f"Failed to save cookies locally to {config.cookie_path}: {save_err}")

    except Exception as e:
        logger.exception(f"An error occurred during the browser login process: {e}")
    finally:
        # --- Cleanup --- #
        if driver:
            try:
                driver.quit()
                logger.info("Browser window closed.")
            except Exception as quit_err:
                 logger.warning(f"Error closing browser window: {quit_err}") # Changed to warning

    # --- End of merged ensure_authentication logic --- #

    # Check the final success flag
    if login_and_upload_success:
        logger.info("Authentication and cookie upload process completed successfully.")
    else:
        logger.error("Authentication process failed. See previous logs for details.")
        sys.exit(1) # Exit with error if auth failed


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        # Use basic logger if setup failed earlier
        logging.getLogger().info("Login process interrupted by user.")
        sys.exit(0)
