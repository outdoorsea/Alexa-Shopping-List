"""Application entrypoint."""

import logging
import argparse
import asyncio
import sys

# Add src directory to path if running directly
# This might not be needed if installed as a package
import os
src_dir = os.path.join(os.path.dirname(__file__), 'src')
if os.path.isdir(src_dir) and src_dir not in sys.path:
    sys.path.insert(0, src_dir)

try:
    from alexa_shopping_list.config import load_config
    # Import run_check and AppConfig (needed for type hint if we were using main_loop)
    from alexa_shopping_list.main import run_check, AppConfig
except ImportError as e:
    print(f"Error importing application modules: {e}", file=sys.stderr)
    print("Ensure you are running from the project root directory or have installed the package.", file=sys.stderr)
    sys.exit(1)

# Basic Logging Setup (before config is loaded)
logging.basicConfig(
    level=logging.INFO, # Default level, will be updated by config
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)
logger = logging.getLogger()

def setup_logging(level_name: str):
    """Sets the root logger level."""
    level = getattr(logging, level_name.upper(), logging.INFO)
    logger.setLevel(level)
    # Also update handlers if needed, but basicConfig usually sets the root handler level
    for handler in logger.handlers:
        handler.setLevel(level)
    logger.info(f"Logging level set to {level_name.upper()}")

def parse_arguments():
    """Parses command line arguments."""
    parser = argparse.ArgumentParser(description='Run the Alexa Shopping List checker.')
    parser.add_argument(
        '--interval',
        type=int,
        default=60,
        help='Interval in seconds between list checks (default: 60)'
    )
    return parser.parse_args()

if __name__ == "__main__":
    # Argument parsing is not needed if we only run the check once
    # args = parse_arguments()

    try:
        config = load_config()
        setup_logging(config.log_level) # Apply log level from config
        logger.info("Starting Alexa Shopping List Check...")
        # Call run_check directly to list items once
        asyncio.run(run_check(config))
    except EnvironmentError as e:
        logger.critical(f"Configuration error: {e}")
        sys.exit(1)
    except KeyboardInterrupt:
        logger.info("Application interrupted by user. Exiting.")
        sys.exit(0)
    except Exception as e:
        logger.exception(f"An unexpected critical error occurred: {e}")
        sys.exit(1)
