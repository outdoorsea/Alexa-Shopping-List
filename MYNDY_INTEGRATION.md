# Myndy-Brain Integration Guide

This guide explains how to integrate the Alexa Shopping List MCP server with myndy-brain.

## Architecture

The integration uses an HTTP MCP server that wraps the Alexa Shopping List API:

```
myndy-brain → HTTP MCP Server (port 8091) → Alexa API Server (port 8000) → Amazon Alexa
```

## Setup

### 1. Prerequisites

Make sure you have completed the main setup from the README:

- API server running: `docker compose up -d alexa_api`
- Cookies authenticated (see README steps 5-7)
- Virtual environment set up with dependencies

### 2. Start the HTTP MCP Server

From the `Alexa-Shopping-List` directory:

```bash
./start-http-mcp.sh
```

The server will start on port 8091 and expose the following endpoints:
- `http://localhost:8091/health` - Health check
- `http://localhost:8091/tools` - List available tools
- `http://localhost:8091/tools/execute` - Execute a tool
- `http://localhost:8091/docs` - Interactive API documentation

### 3. Configure myndy-brain

The configuration has already been added to `~/myndy-core/myndy-brain/config.yaml`:

```yaml
mcp:
  enabled: true
  servers:
    - name: "alexa-shopping-list"
      url: "http://localhost:8091"
      enabled: true
      description: "Alexa Shopping List: add, remove, view, and manage shopping list items"
      timeout: 30.0
```

### 4. Restart myndy-brain

Restart myndy-brain to load the new MCP server:

```bash
cd ~/myndy-core/myndy-brain
./myndy restart
```

## Available Tools

The following tools are available in myndy-brain:

1. **get_all_shopping_items** - Get all items (active and completed)
2. **get_incomplete_shopping_items** - Get only active items
3. **get_completed_shopping_items** - Get only completed items
4. **add_shopping_item** - Add one or more items (single string or array)
5. **delete_shopping_item** - Delete one or more items by name
6. **mark_shopping_item_completed** - Mark items as completed
7. **mark_shopping_item_incomplete** - Mark items as incomplete

## Usage Examples

Once integrated, you can interact with your shopping list through myndy-brain:

```
You: "What's on my shopping list?"
Myndy: [calls get_incomplete_shopping_items tool]

You: "Add milk and eggs to my shopping list"
Myndy: [calls add_shopping_item with ["milk", "eggs"]]

You: "Mark bread as completed"
Myndy: [calls mark_shopping_item_completed with "bread"]
```

## Troubleshooting

### HTTP MCP Server won't start

- Check if port 8091 is available: `lsof -i :8091`
- Check if virtual environment has required dependencies:
  ```bash
  source .venv/bin/activate
  pip install fastapi uvicorn requests pydantic
  ```

### "Could not connect to Alexa API server"

- Ensure API server is running: `docker compose ps alexa_api`
- Check API server logs: `docker compose logs alexa_api`
- Verify API is responding: `curl http://localhost:8000/`

### myndy-brain can't connect to MCP server

- Check HTTP MCP server is running and responding:
  ```bash
  curl http://localhost:8091/health
  ```
- Check myndy-brain logs for connection errors
- Verify the configuration in `config.yaml` has `enabled: true`

### Authentication errors (401)

- Re-run the authentication script:
  ```bash
  source .venv/bin/activate
  python -m src.auth.login
  ```
- Amazon cookies expire periodically and need to be refreshed

## Running as a Service

To keep the HTTP MCP server running in the background, you can use a process manager like `pm2` or `systemd`, or simply run it in a screen/tmux session:

```bash
# Using screen
screen -S alexa-mcp
./start-http-mcp.sh
# Press Ctrl+A, then D to detach

# To reattach later
screen -r alexa-mcp
```

## Architecture Details

### Why HTTP MCP?

The original Alexa Shopping List uses stdio-based MCP (FastMCP), but myndy-brain expects HTTP-based MCP servers. The `http_mcp_server.py` acts as an adapter:

- **Input**: HTTP requests from myndy-brain's MCP client
- **Processing**: Routes requests to the appropriate Alexa API endpoint
- **Output**: Returns results in myndy-brain's expected format

### Port Configuration

- **8000**: Alexa API Server (FastAPI in Docker)
- **8091**: HTTP MCP Server (FastAPI, local)

### Security

- The HTTP MCP server only accepts connections from localhost
- No authentication is required between myndy-brain and the MCP server (both local)
- Authentication with Amazon is handled by the API server using cookies

## Support

For issues specific to:
- **Alexa Shopping List**: See main [README.md](README.md)
- **myndy-brain**: Check myndy-brain documentation
- **This integration**: Open an issue with details about both systems
