import sys
import os
import logging
from typing import List, Dict, Any

# --- Path Modification ---
# Add the project root directory to the Python path
# This allows importing modules from the 'src' directory (e.g., alexa_shopping_list)
project_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
if project_root not in sys.path:
    sys.path.append(project_root)
# --- End Path Modification ---

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field  # For request body validation

# Import necessary components from your existing code
try:
    from alexa_shopping_list.config import load_config, AppConfig
    from alexa_shopping_list.alexa_api import (
        get_shopping_list_items,
        add_shopping_list_item,
        delete_shopping_list_item,
        mark_item_as_completed,
        unmark_item_as_completed,
        filter_incomplete_items,
        # No filter_completed_items, we'll do it inline
    )
except ImportError as e:
    print(f"FATAL ERROR: Could not import alexa_shopping_list modules: {e}", file=sys.stderr)
    print("Ensure the script is run from the project root or the src directory is in PYTHONPATH.", file=sys.stderr)
    sys.exit(1)

# --- Globals & Setup ---

# Configure basic logging
# Note: Uvicorn will likely handle more advanced logging config when run
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Load configuration at startup
# Use the absolute path derived earlier
config: AppConfig
try:
    logger.info(f"Loading configuration using project_root: {project_root}")
    config = load_config(project_root=project_root)
    # Suppress noisy library logs based on loaded config
    log_level = getattr(logging, config.log_level.upper(), logging.INFO)
    if log_level > logging.DEBUG:
        logging.getLogger("urllib3").setLevel(logging.WARNING)
        logging.getLogger("selenium").setLevel(logging.WARNING)
        logging.getLogger("webdriver_manager").setLevel(logging.WARNING)
        logger.debug("Suppressed noisy library logs.")

except Exception as e:
    logger.critical(f"FATAL: Failed to load configuration on startup: {e}", exc_info=True)
    # In a real app, you might want a more robust way to handle this,
    # but for simplicity, we'll exit if config fails.
    # Alternatively, raise an exception that FastAPI/Uvicorn might catch.
    sys.exit("Failed to load application configuration.")

# --- FastAPI App Instance ---
app = FastAPI(
    title="Alexa Shopping List API",
    description="API to interact with an Alexa Shopping List using pre-generated cookies.",
    version="1.0.0"
)

# --- Helper Function ---
def find_item_by_name(items: List[Dict[str, Any]], name: str) -> Dict[str, Any] | None:
    """Finds the first item in a list matching the name (case-insensitive)."""
    if items is None:
        return None
    for item in items:
        if item.get("value", "").lower() == name.lower():
            return item
    return None

# --- Pydantic Models (for Request Bodies) ---
class ItemNameModel(BaseModel):
    item_name: str = Field(..., description="The name of the shopping list item.")

# --- API Endpoints ---

@app.get("/", tags=["Status"])
async def read_root():
    """Simple health check endpoint."""
    return {"status": "Alexa Shopping List API is running"}

@app.get("/items/all", tags=["Items"], response_model=List[Dict[str, Any]])
async def get_all_list_items():
    """Retrieves all items (completed and incomplete) from the shopping list."""
    logger.info("Endpoint GET /items/all called.")
    items = get_shopping_list_items(config)
    if items is None:
        logger.error("Failed to retrieve items from Alexa API.")
        raise HTTPException(status_code=503, detail="Could not retrieve shopping list from Alexa.")
    return items

@app.get("/items/incomplete", tags=["Items"], response_model=List[Dict[str, Any]])
async def get_incomplete_list_items():
    """Retrieves only the incomplete items from the shopping list."""
    logger.info("Endpoint GET /items/incomplete called.")
    all_items = get_shopping_list_items(config)
    if all_items is None:
        logger.error("Failed to retrieve items from Alexa API.")
        raise HTTPException(status_code=503, detail="Could not retrieve shopping list from Alexa.")
    incomplete_items = filter_incomplete_items(all_items)
    return incomplete_items

@app.get("/items/completed", tags=["Items"], response_model=List[Dict[str, Any]])
async def get_completed_list_items():
    """Retrieves only the completed items from the shopping list."""
    logger.info("Endpoint GET /items/completed called.")
    all_items = get_shopping_list_items(config)
    if all_items is None:
        logger.error("Failed to retrieve items from Alexa API.")
        raise HTTPException(status_code=503, detail="Could not retrieve shopping list from Alexa.")
    # Filter completed items directly
    completed_items = [item for item in all_items if item.get('completed', False)]
    return completed_items

@app.post("/items", tags=["Items"], status_code=201)  # 201 Created
async def add_new_item(item_data: ItemNameModel):
    """Adds a new item to the shopping list."""
    item_name = item_data.item_name
    logger.info(f"Endpoint POST /items called to add: '{item_name}'")
    success = add_shopping_list_item(config, item_name)
    if not success:
        logger.error(f"Failed to add item '{item_name}' via Alexa API.")
        raise HTTPException(status_code=500, detail=f"Failed to add item '{item_name}'.")
    return {"message": f"Item '{item_name}' added successfully."}

@app.delete("/items", tags=["Items"])
async def remove_item(item_data: ItemNameModel):
    """Deletes an item from the shopping list by name (case-insensitive)."""
    item_name = item_data.item_name
    logger.info(f"Endpoint DELETE /items called for: '{item_name}'")
    all_items = get_shopping_list_items(config)
    item_to_delete = find_item_by_name(all_items or [], item_name)

    if not item_to_delete:
        logger.warning(f"Item '{item_name}' not found for deletion.")
        raise HTTPException(status_code=404, detail=f"Item '{item_name}' not found.")

    success = delete_shopping_list_item(config, item_to_delete)
    if not success:
        logger.error(f"Failed to delete item '{item_name}' via Alexa API.")
        raise HTTPException(status_code=500, detail=f"Failed to delete item '{item_name}'.")
    return {"message": f"Item '{item_name}' deleted successfully."}

@app.put("/items/mark_completed", tags=["Items"])
async def mark_item_complete(item_data: ItemNameModel):
    """Marks an item as completed by name (case-insensitive)."""
    item_name = item_data.item_name
    logger.info(f"Endpoint PUT /items/mark_completed called for: '{item_name}'")
    all_items = get_shopping_list_items(config)
    # Find an *incomplete* item matching the name
    item_to_mark = find_item_by_name(filter_incomplete_items(all_items or []), item_name)

    if not item_to_mark:
        logger.warning(f"Incomplete item '{item_name}' not found to mark complete.")
        raise HTTPException(status_code=404, detail=f"Incomplete item '{item_name}' not found.")

    success = mark_item_as_completed(config, item_to_mark)
    if not success:
        logger.error(f"Failed to mark item '{item_name}' completed via Alexa API.")
        raise HTTPException(status_code=500, detail=f"Failed to mark item '{item_name}' as completed.")
    return {"message": f"Item '{item_name}' marked as completed."}

@app.put("/items/mark_incomplete", tags=["Items"])
async def mark_item_incomplete_endpoint(item_data: ItemNameModel):
    """Marks an item as incomplete by name (case-insensitive)."""
    item_name = item_data.item_name
    logger.info(f"Endpoint PUT /items/mark_incomplete called for: '{item_name}'")
    all_items = get_shopping_list_items(config)
    # Find a *complete* item matching the name
    completed_items = [item for item in (all_items or []) if item.get('completed', False)]
    item_to_mark = find_item_by_name(completed_items, item_name)

    if not item_to_mark:
        logger.warning(f"Completed item '{item_name}' not found to mark incomplete.")
        raise HTTPException(status_code=404, detail=f"Completed item '{item_name}' not found.")

    success = unmark_item_as_completed(config, item_to_mark)  # Use the correct function
    if not success:
        logger.error(f"Failed to mark item '{item_name}' incomplete via Alexa API.")
        raise HTTPException(status_code=500, detail=f"Failed to mark item '{item_name}' as incomplete.")
    return {"message": f"Item '{item_name}' marked as incomplete."}

# --- Optional: Add main block to run with uvicorn for direct execution ---
if __name__ == "__main__":
    import uvicorn
    logger.info("Starting Uvicorn server directly for development...")
    # Note: Host '0.0.0.0' makes it accessible on your network
    # Use '127.0.0.1' for local access only
    # Reload=True is for development, disable for production
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
