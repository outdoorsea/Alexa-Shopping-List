# Alexa Shopping List Console Output

This project allows incomplete items on your Alexa shopping
list to be outputted to the console and marked as completed on Alexa.
It uses Selenium to handle the initial login via a browser window.

## Features

- Uses Selenium to open a browser for manual user login (handles 2FA).
- Saves authentication cookies after successful browser login.
- Checks Alexa shopping list for incomplete items using saved cookies.
- Outputs incomplete items to the console.
- Marks items as completed on Alexa once they are outputted.
- Periodic execution ensured by python script running in a Docker container.

## Prerequisites

- Docker and Docker Compose (for running via Docker)
- Python 3.x and pip (for running locally)
- **Google Chrome** (or another supported browser) installed on the host machine.
- An Amazon account with Alexa enabled.

## Setup

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```
This will install `requests`, `python-dotenv`, `selenium`, and `webdriver-manager`.
`webdriver-manager` will automatically download the correct ChromeDriver when the script runs.

### 2. Environment Variables

Create a `.env` file in the project root. Populate it with:

```dotenv
# Your local Amazon domain (e.g., amazon.com, amazon.co.uk)
AMAZON_URL=https://www.amazon.com

# Optional: Your Amazon account email (if set, avoids one prompt during login)
# AMAZON_EMAIL=

# Path where the script will SAVE the cookie file (e.g., ./alexa_cookie.pickle)
# Ensure the directory exists if not using the current directory.
COOKIE_PATH=./alexa_cookie.pickle

# Logging level (DEBUG, INFO, WARNING, ERROR)
LOG_LEVEL=INFO
```
*Note: `AMAZON_PASSWORD` and `AMAZON_OTP_SECRET` are no longer used.* Password and 2FA are entered directly in the browser during the Selenium login step.

### 3. Docker Compose (If using Docker)

Update the `docker-compose.yml` file:
1.  Ensure the `COOKIE_PATH` directory is mapped as a volume.
2.  Consider if you need to run the browser headlessly (may require additional setup in `auth.py` and Dockerfile configuration for a headless browser environment).

Example `docker-compose.yml` mapping `./app_data_host` to `/app-data`:
```yaml
services:
  scraper:
    build: . # Build from Dockerfile
    restart: unless-stopped
    container_name: alexa_list_checker
    env_file:
      - .env
    volumes:
      - .:/usr/src/app # Maps project code
      # Map a local directory to store the cookie file
      - ./app_data_host:/app-data
    command: python run.py
```
Make sure the corresponding `.env` has `COOKIE_PATH=/app-data/alexa_cookie.pickle`.
*Running Selenium (especially non-headless) inside Docker requires careful setup of the Docker image (installing Chrome, drivers, potentially Xvfb). The provided Dockerfile might need adjustments.*

### 4. Run

**First Run / Login (Requires Browser Interaction):**
When you run the script for the first time, or if the cookie file (`COOKIE_PATH`) is missing/invalid:
1. Selenium will automatically download the appropriate WebDriver (e.g., ChromeDriver).
2. A browser window (e.g., Chrome) will open to your `AMAZON_URL`.
3. **MANUALLY** log in to your Amazon account in that browser window. Enter your email (if not pre-filled), password, and complete any 2FA steps presented by Amazon.
4. Once you are fully logged in on the main Amazon page, switch back to the console/terminal where the script is running.
5. Press `Enter` in the console.
6. The script will extract the cookies from the browser and save them to `COOKIE_PATH`.
7. The browser window will close.

**Subsequent Runs:**
If a valid cookie file exists at `COOKIE_PATH`, the script will load it and proceed directly to checking the shopping list without opening a browser.

**Running with Docker:**
```bash
# Ensure ./app_data_host (or your mapped directory) exists
mkdir -p ./app_data_host
# Build the image
docker-compose build
# Run (will open browser on host if not headless & configured correctly)
docker-compose up
# Or run detached and check logs:
# docker-compose up -d
# docker-compose logs -f
```
*Note: Running browser automation in Docker can be complex. You might need to run `docker-compose up` without `-d` initially to see browser interaction.*

**Running Locally:**
```bash
# Ensure .env file is populated
# Run the script (will open browser for login if needed)
python3 run.py
```

## Troubleshooting

- **WebDriver Errors:** Ensure Google Chrome is installed and up-to-date. `webdriver-manager` usually handles driver versions, but sometimes manual intervention or clearing its cache (`~/.wdm`) might be needed. Check error logs for specifics.
- **Cookie Extraction Failure:** Make sure you fully complete the login (including 2FA) in the browser *before* pressing Enter in the console.
- **Docker Issues:** Running Selenium in Docker requires the container to have a browser, the correct driver, and potentially a virtual display (like Xvfb) installed. The base `Dockerfile` may need significant additions for this.
- **Expired Cookies:** If the script fails to fetch the list after previously working, the cookies might have expired. Delete the cookie file specified by `COOKIE_PATH` and rerun the script to trigger the browser login again.
