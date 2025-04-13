"""Authentication handling using Selenium for browser-based login."""

import pickle
import logging
import time
from pathlib import Path
from typing import Optional, Dict
import sys

# Selenium Imports
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
# Add Firefox/Edge/etc. imports if needed

from .config import AppConfig

logger = logging.getLogger(__name__)

# --- Selenium Authentication --- #

def format_selenium_cookies(selenium_cookies: list) -> Dict[str, str]:
    """Converts Selenium cookie list to a simple key-value dictionary."""
    return {cookie['name']: cookie['value'] for cookie in selenium_cookies}

async def ensure_authentication(config: AppConfig) -> bool:
    """Ensures valid authentication cookies exist, initiates Selenium login if not.

    Requires user to log in manually via the opened browser window.

    Args:
        config: The application configuration.

    Returns:
        True if cookies are valid or login succeeds, False otherwise.
    """
    cookie_file = Path(config.cookie_path)

    # Try loading existing cookies first
    if cookie_file.is_file():
        logger.info(f"Attempting to use existing cookie.")
        try:
            with open(cookie_file, 'rb') as f:
                loaded_cookies = pickle.load(f)
            # TODO: Add a real API call check here using the loaded cookies
            # to ensure they haven't expired.
            logger.info("Existing cookie file loaded successfully.")
            return True
        except Exception as e:
            logger.warning(f"Could not load or use cookie file ({e}), attempting browser login.")
            cookie_file.unlink(missing_ok=True)

    logger.info("Cookie file not found or invalid. Starting browser login process.")
    logger.info("Setting up Selenium WebDriver...")

    driver = None
    login_success = False
    try:
        # --- Initialize WebDriver (using Chrome as default) ---
        # webdriver-manager will download/cache the correct driver
        # Add options if needed (e.g., headless, user-agent)
        options = webdriver.ChromeOptions()
        # options.add_argument("--headless") # Uncomment for headless mode (might not work with interactive login)
        try:
            service = ChromeService(ChromeDriverManager().install())
            driver = webdriver.Chrome(service=service, options=options)
        except Exception as webdriver_err:
             logger.error("Failed to initialize Chrome WebDriver.")
             logger.error("Ensure Google Chrome is installed and accessible.")
             logger.error(f"Error details: {webdriver_err}")
             print("\nPlease ensure Google Chrome is installed.", file=sys.stderr)
             # Consider adding support for other browsers (Firefox/Edge) here
             return False

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

        # --- Extract and Save Cookies --- #
        logger.info("Attempting to extract cookies from browser...")
        selenium_cookies = driver.get_cookies()

        if not selenium_cookies:
            logger.error("Failed to extract cookies from the browser after login.")
            logger.error("Please ensure you were fully logged in before pressing Enter.")
        else:
            logger.info(f"Successfully extracted {len(selenium_cookies)} cookies.")
            formatted_cookies = format_selenium_cookies(selenium_cookies)

            # Save the cookies
            try:
                with open(cookie_file, 'wb') as f:
                    pickle.dump(formatted_cookies, f)
                logger.info(f"Cookies saved successfully to {config.cookie_path}")
                login_success = True
            except Exception as save_err:
                logger.error(f"Failed to save cookies to {config.cookie_path}: {save_err}")

    except Exception as e:
        logger.exception(f"An error occurred during the browser login process: {e}")
    finally:
        # --- Cleanup --- #
        if driver:
            try:
                driver.quit()
                logger.info("Browser window closed.")
            except Exception as quit_err:
                 logger.error(f"Error closing browser window: {quit_err}")

    if not login_success:
         logger.error("Browser-based login process failed to obtain valid cookies.")

    return login_success
