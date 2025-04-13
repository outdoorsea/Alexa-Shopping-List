"""Main application loop for checking Alexa shopping list."""

import logging
import asyncio
import sys

from .config import load_config, AppConfig
from .auth import ensure_authentication
from .alexa_api import (
    get_shopping_list_items,
    filter_incomplete_items,
    mark_item_as_completed,
    add_shopping_list_item
)

logger = logging.getLogger(__name__)

async def run_check(config: AppConfig):
    """Performs a single check for incomplete items and processes them."""

    # Ensure authenticated
    if not await ensure_authentication(config):
        logger.critical("Authentication failed. Cannot proceed with check.")
        return # Skip this check cycle

    # Get shopping list items
    all_items = get_shopping_list_items(config)
    if all_items is None:
        logger.error("Could not retrieve shopping list items.")
        return # Skip this check cycle

    if not all_items:
        logger.info("Shopping list is empty.")
        return # Nothing to process

    # Filter for incomplete items
    incomplete_items = filter_incomplete_items(all_items)
    if not incomplete_items:
        logger.info("No incomplete items found on the shopping list.")
        return # Nothing to process
    # Process incomplete items
    print("SHOPPING LIST ITEMS:")
    for item in incomplete_items:
        item_name = item.get("value", "<Unknown Item>")
        item_id = item.get("id", "<Unknown ID>")
        print(f"- {item_name} (ID: {item_id})")

async def main_loop(config: AppConfig, interval_seconds: int):
    """Runs the check loop indefinitely."""
    while True:
        try:
            await run_check(config)
        except Exception as e:
            # Catch exceptions during the check itself to prevent loop crash
            logger.exception(f"Unexpected error during run_check: {e}")

        logger.info(f"Waiting for {interval_seconds} seconds...")
        await asyncio.sleep(interval_seconds)

if __name__ == "__main__":
    # Load configuration using the dedicated function
    config = load_config()

    # Setup logging
    log_level_str = config.log_level.upper()
    log_level = getattr(logging, log_level_str, logging.INFO)
    logging.basicConfig(
        level=log_level,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        stream=sys.stdout # Log to stdout
    )
    if log_level > logging.DEBUG:
         # Suppress noisy library logs unless debugging
         logging.getLogger("urllib3").setLevel(logging.WARNING)
         logging.getLogger("selenium").setLevel(logging.INFO)
         logging.getLogger("webdriver_manager").setLevel(logging.INFO)

    logger.info("Application starting...")

    # Execute the check sequence (which now only lists items)
    try:
        asyncio.run(run_check(config))
    except KeyboardInterrupt:
        logger.info("Application stopped by user.")
    except Exception as e:
        logger.exception(f"An unexpected error occurred at the top level: {e}")
        sys.exit(1)

    logger.info("Application finished.")
