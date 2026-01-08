"""
HTTP MCP Server for Alexa Shopping List

This server wraps the Alexa Shopping List API and exposes it via HTTP
endpoints compatible with myndy-brain's MCP client.

Port: 8091 (configurable)
Endpoints:
  - GET  /health - Health check
  - GET  /tools - List available tools
  - POST /tools/execute - Execute a tool

Usage:
  python -m src.mcp.http_mcp_server
"""

import logging
import sys
from typing import Dict, Any, List, Optional, Union
from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel
import uvicorn
import requests

# Import local config
try:
    from . import config as mcp_config
except ImportError:
    print("Error: Could not import MCP config", file=sys.stderr)
    sys.exit(1)

# Configure logging
logging.basicConfig(
    level=mcp_config.LOG_LEVEL_INT,
    format='%(asctime)s - %(name)s [%(levelname)s] %(message)s'
)
logger = logging.getLogger(__name__)

# FastAPI app
app = FastAPI(
    title="Alexa Shopping List MCP Server",
    description="HTTP MCP Server for Alexa Shopping List integration with myndy-brain",
    version="1.0.0"
)

# API configuration
API_BASE_URL = mcp_config.API_BASE_URL
HTTP_SERVER_PORT = 8091  # Different from API port (8000)

# Tool definitions
TOOLS = [
    {
        "name": "get_all_shopping_items",
        "description": "Retrieves all items currently on the Alexa shopping list, including both active (incomplete) and completed items.",
        "category": "shopping",
        "parameters": {
            "type": "object",
            "properties": {},
            "required": []
        }
    },
    {
        "name": "get_incomplete_shopping_items",
        "description": "Retrieves only the active (incomplete) items currently on the Alexa shopping list. Useful for seeing what still needs to be purchased.",
        "category": "shopping",
        "parameters": {
            "type": "object",
            "properties": {},
            "required": []
        }
    },
    {
        "name": "get_completed_shopping_items",
        "description": "Retrieves only the completed items currently on the Alexa shopping list.",
        "category": "shopping",
        "parameters": {
            "type": "object",
            "properties": {},
            "required": []
        }
    },
    {
        "name": "add_shopping_item",
        "description": "Adds one or more new items to the Alexa shopping list. Input can be a single item name or a list of item names.",
        "category": "shopping",
        "parameters": {
            "type": "object",
            "properties": {
                "item_name": {
                    "type": ["string", "array"],
                    "description": "Single item name (string) or list of item names (array of strings)",
                    "items": {"type": "string"}
                }
            },
            "required": ["item_name"]
        }
    },
    {
        "name": "delete_shopping_item",
        "description": "Deletes one or more items from the Alexa shopping list by their exact name (case-insensitive).",
        "category": "shopping",
        "parameters": {
            "type": "object",
            "properties": {
                "item_name": {
                    "type": ["string", "array"],
                    "description": "Single item name (string) or list of item names (array of strings)",
                    "items": {"type": "string"}
                }
            },
            "required": ["item_name"]
        }
    },
    {
        "name": "mark_shopping_item_completed",
        "description": "Marks one or more items on the Alexa shopping list as completed by their exact name (case-insensitive).",
        "category": "shopping",
        "parameters": {
            "type": "object",
            "properties": {
                "item_name": {
                    "type": ["string", "array"],
                    "description": "Single item name (string) or list of item names (array of strings)",
                    "items": {"type": "string"}
                }
            },
            "required": ["item_name"]
        }
    },
    {
        "name": "mark_shopping_item_incomplete",
        "description": "Marks one or more previously completed items on the Alexa shopping list as incomplete (active). Use this if an item was marked completed by mistake.",
        "category": "shopping",
        "parameters": {
            "type": "object",
            "properties": {
                "item_name": {
                    "type": ["string", "array"],
                    "description": "Single item name (string) or list of item names (array of strings)",
                    "items": {"type": "string"}
                }
            },
            "required": ["item_name"]
        }
    },
    {
        "name": "check_alexa_auth_status",
        "description": "Checks if Alexa Shopping List authentication is valid. Returns authentication status and instructions if re-authentication is needed.",
        "category": "shopping",
        "parameters": {
            "type": "object",
            "properties": {},
            "required": []
        }
    }
]


class ToolExecuteRequest(BaseModel):
    """Request model for tool execution"""
    tool_name: str
    parameters: Dict[str, Any] = {}
    stream: bool = False


def make_api_request(method: str, endpoint: str, json_data: Optional[Dict] = None) -> Dict:
    """Makes a request to the Alexa API server"""
    url = f"{API_BASE_URL}{endpoint}"
    logger.debug(f"Making {method} request to API: {url}")

    try:
        if method.upper() == "GET":
            response = requests.get(url, timeout=10)
        elif method.upper() == "POST":
            response = requests.post(url, json=json_data, timeout=10)
        elif method.upper() == "PUT":
            response = requests.put(url, json=json_data, timeout=10)
        elif method.upper() == "DELETE":
            response = requests.delete(url, json=json_data, timeout=10)
        else:
            return {"error": f"Unsupported HTTP method: {method}"}

        response.raise_for_status()

        try:
            return response.json()
        except ValueError:
            return {"message": response.text}

    except requests.exceptions.ConnectionError as e:
        logger.error(f"Connection error: {e}")
        return {"error": f"Could not connect to Alexa API server at {API_BASE_URL}. Is it running?"}
    except requests.exceptions.HTTPError as e:
        logger.error(f"HTTP error: {e}")
        try:
            error_detail = response.json().get("detail", str(e))
        except (ValueError, AttributeError):
            error_detail = str(e)
        return {"error": error_detail}
    except requests.exceptions.Timeout as e:
        logger.error(f"Timeout: {e}")
        return {"error": f"Request timeout: {str(e)}"}
    except Exception as e:
        logger.error(f"Error making API request: {e}")
        return {"error": str(e)}


def execute_tool_logic(tool_name: str, parameters: Dict[str, Any]) -> Dict[str, Any]:
    """Execute a tool and return the result"""
    import time
    start_time = time.time()

    try:
        # Route to appropriate API endpoint based on tool name
        if tool_name == "get_all_shopping_items":
            result = make_api_request("GET", "/items/all")
            success = "error" not in result
            output = result if isinstance(result, list) else result
            error = result.get("error") if not success else None

        elif tool_name == "get_incomplete_shopping_items":
            result = make_api_request("GET", "/items/incomplete")
            success = "error" not in result
            output = result if isinstance(result, list) else result
            error = result.get("error") if not success else None

        elif tool_name == "get_completed_shopping_items":
            result = make_api_request("GET", "/items/completed")
            success = "error" not in result
            output = result if isinstance(result, list) else result
            error = result.get("error") if not success else None

        elif tool_name == "add_shopping_item":
            item_name = parameters.get("item_name")
            if not item_name:
                return {
                    "success": False,
                    "output": None,
                    "error": "Missing required parameter: item_name"
                }

            # Handle single item or list
            item_names = [item_name] if isinstance(item_name, str) else item_name
            results = []
            all_succeeded = True

            for name in item_names:
                if not isinstance(name, str) or not name.strip():
                    results.append({"item": name, "success": False, "message": "Invalid item name"})
                    all_succeeded = False
                    continue

                api_result = make_api_request("POST", "/items", {"item_name": name.strip()})
                item_success = "error" not in api_result
                results.append({
                    "item": name.strip(),
                    "success": item_success,
                    "message": api_result.get("message", api_result.get("error", "Unknown result"))
                })
                if not item_success:
                    all_succeeded = False

            success = all_succeeded
            output = {"results": results}
            error = None if success else "Some items failed to add"

        elif tool_name == "delete_shopping_item":
            item_name = parameters.get("item_name")
            if not item_name:
                return {
                    "success": False,
                    "output": None,
                    "error": "Missing required parameter: item_name"
                }

            item_names = [item_name] if isinstance(item_name, str) else item_name
            results = []
            all_succeeded = True

            for name in item_names:
                if not isinstance(name, str) or not name.strip():
                    results.append({"item": name, "success": False, "message": "Invalid item name"})
                    all_succeeded = False
                    continue

                api_result = make_api_request("DELETE", "/items", {"item_name": name.strip()})
                item_success = "error" not in api_result
                results.append({
                    "item": name.strip(),
                    "success": item_success,
                    "message": api_result.get("message", api_result.get("error", "Unknown result"))
                })
                if not item_success:
                    all_succeeded = False

            success = all_succeeded
            output = {"results": results}
            error = None if success else "Some items failed to delete"

        elif tool_name == "mark_shopping_item_completed":
            item_name = parameters.get("item_name")
            if not item_name:
                return {
                    "success": False,
                    "output": None,
                    "error": "Missing required parameter: item_name"
                }

            item_names = [item_name] if isinstance(item_name, str) else item_name
            results = []
            all_succeeded = True

            for name in item_names:
                if not isinstance(name, str) or not name.strip():
                    results.append({"item": name, "success": False, "message": "Invalid item name"})
                    all_succeeded = False
                    continue

                api_result = make_api_request("PUT", "/items/mark_completed", {"item_name": name.strip()})
                item_success = "error" not in api_result
                results.append({
                    "item": name.strip(),
                    "success": item_success,
                    "message": api_result.get("message", api_result.get("error", "Unknown result"))
                })
                if not item_success:
                    all_succeeded = False

            success = all_succeeded
            output = {"results": results}
            error = None if success else "Some items failed to mark as completed"

        elif tool_name == "mark_shopping_item_incomplete":
            item_name = parameters.get("item_name")
            if not item_name:
                return {
                    "success": False,
                    "output": None,
                    "error": "Missing required parameter: item_name"
                }

            item_names = [item_name] if isinstance(item_name, str) else item_name
            results = []
            all_succeeded = True

            for name in item_names:
                if not isinstance(name, str) or not name.strip():
                    results.append({"item": name, "success": False, "message": "Invalid item name"})
                    all_succeeded = False
                    continue

                api_result = make_api_request("PUT", "/items/mark_incomplete", {"item_name": name.strip()})
                item_success = "error" not in api_result
                results.append({
                    "item": name.strip(),
                    "success": item_success,
                    "message": api_result.get("message", api_result.get("error", "Unknown result"))
                })
                if not item_success:
                    all_succeeded = False

            success = all_succeeded
            output = {"results": results}
            error = None if success else "Some items failed to mark as incomplete"

        elif tool_name == "check_alexa_auth_status":
            # Try to fetch items to test authentication
            result = make_api_request("GET", "/items/incomplete")

            if "error" in result:
                error_msg = str(result.get("error", ""))
                if "401" in error_msg or "Unauthorized" in error_msg or "expired" in error_msg.lower():
                    # Authentication expired
                    success = True  # Tool succeeded, but auth is invalid
                    output = {
                        "authenticated": False,
                        "status": "expired",
                        "message": "Amazon authentication has expired. Re-authentication required.",
                        "instructions": "To re-authenticate:\n1. Open terminal\n2. Run: cd ~/Alexa-Shopping-List && ./login.sh\n3. Log in to Amazon when browser opens\n4. Press Enter after successful login\n\nNote: Amazon cookies expire periodically and require manual re-authentication."
                    }
                    error = None
                else:
                    # Other error (API not running, etc.)
                    success = False
                    output = {
                        "authenticated": "unknown",
                        "status": "error",
                        "message": f"Could not check authentication status: {error_msg}"
                    }
                    error = error_msg
            elif isinstance(result, list):
                # Successfully got items - authentication is valid
                success = True
                output = {
                    "authenticated": True,
                    "status": "valid",
                    "message": "Amazon authentication is valid and working.",
                    "items_count": len(result)
                }
                error = None
            else:
                # Unexpected response
                success = False
                output = {
                    "authenticated": "unknown",
                    "status": "unexpected_response",
                    "message": "Received unexpected response from API"
                }
                error = "Unexpected API response format"

        else:
            return {
                "success": False,
                "output": None,
                "error": f"Unknown tool: {tool_name}"
            }

        execution_time = time.time() - start_time
        return {
            "success": success,
            "output": output,
            "error": error,
            "execution_time": execution_time
        }

    except Exception as e:
        logger.exception(f"Error executing tool {tool_name}: {e}")
        execution_time = time.time() - start_time
        return {
            "success": False,
            "output": None,
            "error": str(e),
            "execution_time": execution_time
        }


# HTTP Endpoints

@app.get("/health")
async def health_check():
    """Health check endpoint"""
    # Check if API server is accessible
    try:
        api_response = make_api_request("GET", "/")
        api_accessible = "error" not in api_response
    except Exception:
        api_accessible = False

    status = "healthy" if api_accessible else "degraded"

    return {
        "status": status,
        "service": "alexa-shopping-list-mcp",
        "api_server": {
            "url": API_BASE_URL,
            "accessible": api_accessible
        }
    }


@app.get("/tools")
async def list_tools(
    limit: int = 100,
    category: Optional[str] = None,
    search: Optional[str] = None
):
    """List available tools"""
    tools = TOOLS.copy()

    # Filter by category
    if category:
        tools = [t for t in tools if t.get("category") == category]

    # Filter by search
    if search:
        search_lower = search.lower()
        tools = [
            t for t in tools
            if search_lower in t["name"].lower() or search_lower in t["description"].lower()
        ]

    # Apply limit
    tools = tools[:limit]

    return {
        "tools": tools,
        "total": len(tools)
    }


@app.post("/tools/execute")
async def execute_tool(request: ToolExecuteRequest):
    """Execute a tool"""
    logger.info(f"Executing tool: {request.tool_name}")
    logger.debug(f"Parameters: {request.parameters}")

    # Find tool
    tool = next((t for t in TOOLS if t["name"] == request.tool_name), None)
    if not tool:
        raise HTTPException(status_code=404, detail=f"Tool not found: {request.tool_name}")

    # Execute tool
    result = execute_tool_logic(request.tool_name, request.parameters)

    return {
        "tool_name": request.tool_name,
        "result": result
    }


@app.get("/")
async def root():
    """Root endpoint"""
    return {
        "service": "Alexa Shopping List MCP Server",
        "version": "1.0.0",
        "api_server": API_BASE_URL,
        "tools_count": len(TOOLS)
    }


if __name__ == "__main__":
    logger.info(f"Starting HTTP MCP Server on port {HTTP_SERVER_PORT}")
    logger.info(f"API Server: {API_BASE_URL}")

    uvicorn.run(
        app,
        host="0.0.0.0",
        port=HTTP_SERVER_PORT,
        log_level="info"
    )
