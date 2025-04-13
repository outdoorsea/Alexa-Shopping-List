#!/Users/sethrose/Developer/github/Temp/alexa-mcp/.venv/bin/python
import sys
import os
import logging
import requests  # For making API calls
import json
from typing import List, Dict, Any, Optional

# --- Path Modification ---
# No longer need to add project root to path since we don't directly import alexa_shopping_list modules
# Now we just make HTTP requests to our FastAPI server
# --- End Path Modification ---

from fastmcp import FastMCP

# Configure basic logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# API server configuration
API_BASE_URL = "http://127.0.0.1:8000"  # Default URL for the FastAPI server

# --- FastMCP Server Instance ---
mcp = FastMCP("Alexa Shopping List")

# --- Helper Functions ---
def make_api_request(method: str, endpoint: str, json_data: Optional[Dict] = None) -> Dict:
    """Makes a request to the FastAPI server and handles errors."""
    url = f"{API_BASE_URL}{endpoint}"
    logger.debug(f"Making {method} request to FastAPI: {url}")

    try:
        if method.upper() == "GET":
            response = requests.get(url)
        elif method.upper() == "POST":
            response = requests.post(url, json=json_data)
        elif method.upper() == "PUT":
            response = requests.put(url, json=json_data)
        elif method.upper() == "DELETE":
            response = requests.delete(url, json=json_data)
        else:
            logger.error(f"Unsupported HTTP method: {method}")
            return {"error": f"Unsupported HTTP method: {method}"}

        # Raise exception for 4xx/5xx status codes
        response.raise_for_status()

        # Try to parse JSON, fall back to text if not JSON
        try:
            return response.json()
        except json.JSONDecodeError:
            return {"message": response.text}

    except requests.exceptions.ConnectionError:
        logger.error(f"Connection error: Could not connect to FastAPI server at {API_BASE_URL}")
        return {"error": "Could not connect to FastAPI server. Is it running?"}
    except requests.exceptions.HTTPError as e:
        logger.error(f"HTTP error: {e}")
        # Try to get error details from the response
        try:
            error_detail = response.json().get("detail", str(e))
        except (json.JSONDecodeError, AttributeError):
            error_detail = str(e)
        return {"error": error_detail}
    except Exception as e:
        logger.error(f"Error making API request: {e}")
        return {"error": str(e)}

# --- Tool Definitions ---
# These now proxy requests to our FastAPI server

@mcp.tool()
def get_all_items() -> list[dict]:
    """Retrieves all items (both complete and incomplete) from the Alexa shopping list."""
    logger.info("Tool 'get_all_items' called.")
    response = make_api_request("GET", "/items/all")

    if "error" in response:
        logger.error(f"Error in get_all_items: {response['error']}")
        return []  # Return empty list on error

    # Make sure we return a list even if API somehow returns something else
    if isinstance(response, list):
        return response  # API already returns the list format we need
    else:
        logger.warning(f"Unexpected response format from API, expected list but got: {type(response)}")
        return []

@mcp.tool()
def get_incomplete_items() -> list[dict]:
    """Retrieves only the incomplete items from the Alexa shopping list."""
    logger.info("Tool 'get_incomplete_items' called.")
    response = make_api_request("GET", "/items/incomplete")

    if "error" in response:
        logger.error(f"Error in get_incomplete_items: {response['error']}")
        return []

    # Make sure we return a list even if API somehow returns something else
    if isinstance(response, list):
        return response
    else:
        logger.warning(f"Unexpected response format from API, expected list but got: {type(response)}")
        return []

@mcp.tool()
def get_completed_items() -> list[dict]:
    """Retrieves only the completed items from the Alexa shopping list."""
    logger.info("Tool 'get_completed_items' called.")
    response = make_api_request("GET", "/items/completed")

    if "error" in response:
        logger.error(f"Error in get_completed_items: {response['error']}")
        return []

    # Make sure we return a list even if API somehow returns something else
    if isinstance(response, list):
        return response
    else:
        logger.warning(f"Unexpected response format from API, expected list but got: {type(response)}")
        return []

@mcp.tool()
def add_item(item_name: str) -> dict:
    """Adds a new item to the Alexa shopping list."""
    logger.info(f"Tool 'add_item' called with item_name: '{item_name}'")
    response = make_api_request("POST", "/items", {"item_name": item_name})

    # Return a standardized response dictionary
    if "error" in response:
        logger.error(f"Error in add_item: {response['error']}")
        return {"success": False, "message": response["error"]}

    return {"success": True, "message": response.get("message", "Item added successfully.")}

@mcp.tool()
def delete_item(item_name: str) -> dict:
    """
    Deletes an item from the Alexa shopping list by its name.
    Requires an exact match (case-insensitive) of the item name.
    If multiple items have the same name, only one will be deleted.
    Returns a dictionary indicating success or failure.
    """
    logger.info(f"Tool 'delete_item' called with item_name: '{item_name}'")
    response = make_api_request("DELETE", "/items", {"item_name": item_name})

    if "error" in response:
        logger.error(f"Error in delete_item: {response['error']}")
        return {"success": False, "message": response["error"]}

    return {"success": True, "message": response.get("message", "Item deleted successfully.")}

@mcp.tool()
def mark_item_completed(item_name: str) -> dict:
    """
    Marks an item on the Alexa shopping list as completed by its name.
    Requires an exact match (case-insensitive) of the item name.
    If multiple items have the same name, only one will be marked.
    Returns a dictionary indicating success or failure.
    """
    logger.info(f"Tool 'mark_item_completed' called with item_name: '{item_name}'")
    response = make_api_request("PUT", "/items/mark_completed", {"item_name": item_name})

    if "error" in response:
        logger.error(f"Error in mark_item_completed: {response['error']}")
        return {"success": False, "message": response["error"]}

    return {"success": True, "message": response.get("message", "Item marked as completed.")}

@mcp.tool()
def mark_item_incomplete(item_name: str) -> dict:
    """
    Marks an item on the Alexa shopping list as incomplete (active) by its name.
    Requires an exact match (case-insensitive) of the item name.
    If multiple items have the same name, only one will be marked.
    Returns a dictionary indicating success or failure.
    """
    logger.info(f"Tool 'mark_item_incomplete' called with item_name: '{item_name}'")
    response = make_api_request("PUT", "/items/mark_incomplete", {"item_name": item_name})

    if "error" in response:
        logger.error(f"Error in mark_item_incomplete: {response['error']}")
        return {"success": False, "message": response["error"]}

    return {"success": True, "message": response.get("message", "Item marked as incomplete.")}

# --- API Status Check ---
@mcp.tool()
def check_api_status() -> dict:
    """Check if the FastAPI server is running and accessible."""
    logger.info("Tool 'check_api_status' called.")
    response = make_api_request("GET", "/")

    if "error" in response:
        logger.error(f"API status check failed: {response['error']}")
        return {
            "status": "ERROR",
            "message": f"FastAPI server is not accessible: {response['error']}"
        }

    return {
        "status": "OK",
        "message": "FastAPI server is running and accessible.",
        "details": response
    }

# --- Run Server ---
if __name__ == "__main__":
    logger.info("Starting FastMCP server...")
    print("--- MCP Server (Root): Starting ---", file=sys.stderr); sys.stderr.flush()

    # Initial API health check with added error handling
    try:
        print("--- MCP Server (Root): Performing initial API health check... ---", file=sys.stderr); sys.stderr.flush()
        status = check_api_status()
        if status.get("status") == "ERROR":
            logger.warning(f"WARNING: {status.get('message')}. Some tools may not work correctly.")
            print(f"--- MCP Server (Root) WARNING: FastAPI server not accessible during initial check: {status.get('message')} ---", file=sys.stderr)
            sys.stderr.flush()
        else:
            print("--- MCP Server (Root): Initial API health check successful. ---", file=sys.stderr); sys.stderr.flush()
    except Exception as initial_check_error:
        # Catch any unexpected error during the initial check itself
        print(f"--- MCP Server (Root) FATAL ERROR during initial API check: {initial_check_error} ---", file=sys.stderr)
        logger.exception(f"Fatal error during initial API status check: {initial_check_error}")
        import traceback
        traceback.print_exc(file=sys.stderr)
        sys.stderr.flush()
        # Optionally, decide whether to exit here or let mcp.run() potentially fail later
        # For now, we'll log the error and continue to mcp.run()
        print("--- MCP Server (Root): Proceeding to mcp.run() despite initial check error. ---", file=sys.stderr); sys.stderr.flush()

    try:
        print("--- MCP Server (Root): Entering mcp.run() ---", file=sys.stderr); sys.stderr.flush()
        mcp.run()
    except Exception as e:
        print(f"--- MCP Server (Root) FATAL ERROR: Exception from mcp.run(): {e} ---", file=sys.stderr)
        logger.exception(f"Exception from mcp.run(): {e}")  # Log with traceback via logger
        import traceback
        traceback.print_exc(file=sys.stderr)  # Also print traceback directly
        sys.stderr.flush()
        sys.exit(1)  # Ensure exit on error from run
    finally:
        print("--- MCP Server (Root): mcp.run() exited ---", file=sys.stderr); sys.stderr.flush()
        logger.info("FastMCP server finished.")
