# Configuration for the MCP Server
import logging

# Logging level for the MCP server
LOG_LEVEL = "INFO"

# Host and Port where the API container is running
# Assumes API container is accessible on localhost from where MCP server runs
# Using port 8092 to avoid conflict with myndy-ai (which uses 8000)
API_HOST = "localhost"
API_PORT = 8092

# --- Derived --- #
LOG_LEVEL_INT = getattr(logging, LOG_LEVEL.upper(), logging.INFO)
API_BASE_URL = f"http://{API_HOST}:{API_PORT}"
