"""Configuration management using environment variables."""

import os
import logging
from dataclasses import dataclass
from dotenv import load_dotenv
from typing import Optional
import sys

logger = logging.getLogger(__name__)

@dataclass
class AppConfig:
    amazon_url: str
    cookie_path: str
    log_level: str
    api_port: int

def load_config(project_root: Optional[str] = None) -> AppConfig:
    """Loads configuration from .env file and environment variables."""
    try:
        # Determine the .env file path
        if project_root:
            dotenv_path = os.path.join(project_root, '.env')
            print(f"--- Config Loader: Using specified .env path: {dotenv_path} ---", file=sys.stderr); sys.stderr.flush()
            # Check if the specified file exists
            if not os.path.exists(dotenv_path):
                print(f"--- Config Loader WARNING: Specified .env file not found at {dotenv_path} ---", file=sys.stderr); sys.stderr.flush()
                # Fall back to default search if specified path doesn't exist?
                # Or just let load_dotenv handle it / fail?
                # Let load_dotenv handle it for now.
                pass # Explicitly do nothing, load_dotenv below will search if path is None/invalid
            found = load_dotenv(dotenv_path=dotenv_path, override=True)
            if not found:
                print(f"--- Config Loader WARNING: dotenv file not loaded from specified path: {dotenv_path} ---", file=sys.stderr); sys.stderr.flush()
                # Attempt default search as fallback
                print("--- Config Loader: Falling back to default dotenv search. ---", file=sys.stderr); sys.stderr.flush()
                load_dotenv(override=True)
        else:
            print("--- Config Loader: No project_root specified, using default dotenv search. ---", file=sys.stderr); sys.stderr.flush()
            # Default behavior: search up from the script directory or CWD
            load_dotenv(override=True)

        # Validate required environment variables
        amazon_url = os.getenv("AMAZON_URL")
        cookie_path = os.getenv('COOKIE_PATH')
        log_level = os.getenv('LOG_LEVEL', 'INFO').upper()
        # Load API port, default to 8000 if not set or invalid
        api_port_str = os.getenv('API_PORT', '8000')
        try:
            api_port = int(api_port_str)
            if not (1024 <= api_port <= 65535): # Basic port range check
                logger.warning(f"API_PORT '{api_port_str}' is outside typical range (1024-65535), using default 8000.")
                api_port = 8000
        except ValueError:
            logger.warning(f"Invalid API_PORT '{api_port_str}', using default 8000.")
            api_port = 8000

        # Validation
        if not amazon_url:
            logger.critical("Missing required environment variable: AMAZON_URL")
            raise EnvironmentError("Missing required environment variable: AMAZON_URL")
        if not cookie_path:
            logger.critical("Missing required environment variable: COOKIE_PATH")
            raise EnvironmentError("Missing required environment variable: COOKIE_PATH")

        # Validate log level
        if log_level not in ['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL']:
            logger.warning(f"Invalid LOG_LEVEL '{log_level}', defaulting to INFO.")
            log_level = 'INFO'

        logger.info("Configuration loaded.")
        logger.debug(
            f"Config: URL={amazon_url}, CookiePath={cookie_path}, LogLevel={log_level}, ApiPort={api_port}"
        )

        return AppConfig(
            amazon_url=amazon_url,
            cookie_path=cookie_path,
            log_level=log_level,
            api_port=api_port
        )
    except Exception as e:
        logger.critical(f"Error loading configuration: {e}")
        raise
