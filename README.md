# Alexa Shopping List API (Dockerized) + MCP Server

This project allows an LLM (like Claude) to interact with your Alexa shopping list via the Model Context Protocol (MCP). It uses a containerized FastAPI backend and a local MCP server.

1.  **FastAPI Server (Docker Container - `src/api/main.py`):** Runs inside a Docker container. Handles interaction with the Alexa API using cookies injected via an endpoint.
2.  **MCP Server (`src/mcp/mcp_server.py`):** Runs locally. Acts as a proxy, exposing tools via MCP that forward requests to the running Dockerized FastAPI server.
3.  **Login Script (`src/mcp/login.py`):** Runs locally. Uses Selenium to handle Amazon login and then sends the generated cookies to the FastAPI container via its `/auth/cookies` endpoint.

## Features

- Provides MCP tools to:
    - Get all items (`get_all_items`).
    - Get incomplete items (`get_incomplete_items`).
    - Get completed items (`get_completed_items`).
    - Add an item (`add_item`).
    - Delete an item by name (`delete_item`).
    - Mark an item as complete by name (`mark_item_completed`).
    - Mark an item as incomplete by name (`mark_item_incomplete`).
    - Check the status of the backend FastAPI server (`check_api_status`).
- Uses Selenium **in a separate local script** (`src/mcp/login.py`) for initial Amazon login.
- Cookies are **sent to and stored within** the Docker container's persistent volume.
- The containerized FastAPI server loads the injected cookies for authenticated API calls.
- The local MCP server communicates with the Dockerized FastAPI server.

## Prerequisites

- Python 3.x (for local scripts: login, MCP server)
- Docker and Docker Compose (or Docker Desktop)
- A virtual environment tool (like `venv`)
- `pip` (or `uv`)
- **Google Chrome** (or another supported browser) installed on the host machine for the login script.
- An Amazon account with Alexa enabled.

## Getting Started: Step-by-Step

Follow these steps in order to set up and run the system:

**Step 1: Clone the Repository & Configure**

```bash
# 1. Clone the repository
# git clone <repository_url>
cd alexa-mcp

# 2. Create and configure your environment file
cp .env.example .env
# --> EDIT .env with your AMAZON_URL, etc. <--
```

Key variables in `.env`:
```dotenv
# Your local Amazon domain (e.g., amazon.com, amazon.co.uk)
AMAZON_URL=https://www.amazon.com

# Path where the login script will TEMPORARILY save the cookie file before sending it.
COOKIE_PATH=./alexa_cookie.pickle

# Logging level for the scripts (DEBUG, INFO, WARNING, ERROR, CRITICAL)
LOG_LEVEL=INFO

# Port the Dockerized API server will listen on INSIDE the container.
# The login script needs this to know where to send the cookies.
# This MUST match the port in the Dockerfile CMD.
API_PORT=8000

# Optional: Port to EXPOSE the API server on the HOST machine
# Defaults to the internal API_PORT if not set in docker-compose.yml
# HOST_API_PORT=8000
```

**Step 2: Build and Start the API Server Container**

This command builds the Docker image (if needed) and starts the FastAPI server container in the background. It uses the settings from your `.env` file.

```bash
docker compose up --build -d alexa_api
```
- You only need to run `--build` the first time or after changing `Dockerfile` or `requirements.txt`.
- Use `docker compose logs -f alexa_api` to view the container's logs.
- Use `docker compose down` to stop the container when finished.

**Step 3: Authenticate (Run Locally to Inject Cookies)**

This local script interacts with your browser and sends authentication cookies to the running Docker container. **Run this step whenever you need to log in or refresh your credentials.** Running it again will overwrite the existing cookies in the container.

```bash
uv venv
uv pip install -r requirements.txt
python login.py
```

**Browser Interaction during `python login.py`:**
*   Follow the console prompts.
*   Selenium will open a browser window.
*   **MANUALLY** log in to your Amazon account (including 2FA).
*   Once logged in, return to the console and press `Enter`.
*   Cookies are sent to the container. Check logs for confirmation.

**Step 4: Run the MCP Server (Locally)**

With the Dockerized API running and authenticated (Step 2 & 3 done), you can now run the MCP server locally to interact via Claude Desktop or other MCP clients.

**Option A: Direct Execution (for Testing/Development)**

In a terminal (with the virtual environment activated):

```bash
source .venv/bin/activate
python src/mcp/mcp_server.py
```

**Option B: Claude Desktop Integration**

Configure Claude Desktop to run the *local* MCP server script using your virtual environment's Python interpreter.

1.  **Find `mcp.json`:** Locate the configuration file.
2.  **Add/Edit Server Entry:**

    ```json
    {
      "servers": [
        {
          "name": "Alexa Shopping List (Docker Backend)",
          "type": "stdio",
          "command": "/path/to/your/project/alexa-mcp/.venv/bin/python", // <-- ABSOLUTE path
          "args": [
            "/path/to/your/project/alexa-mcp/src/mcp/mcp_server.py" // <-- ABSOLUTE path
          ],
          "workingDirectory": "/path/to/your/project/alexa-mcp" // <-- ABSOLUTE path
        }
        // ... other servers ...
      ]
    }
    ```
    **Important:** Replace `/path/to/your/project/alexa-mcp` with the actual, absolute path.

3.  **Restart Claude Desktop:** If running, restart it.
4.  **Activate Tool:** Use the tool in Claude.

## Troubleshooting

- **MCP Server Fails to Start (Claude Desktop):**
    - **`spawn ... ENOENT`:** Check absolute paths in `mcp.json`.
    - **Immediate Disconnect:** Ensure `alexa_api` container is running. Check MCP/container logs. Ensure MCP can reach API (usually `http://localhost:8000`).
- **API Container Fails to Start or Errors:**
    - Check logs: `docker compose logs alexa_api`.
    - **Configuration Errors:** Ensure `.env` exists and is read by `docker-compose.yml` via `env_file`.
    - **Import Errors:** Verify `COPY` in `Dockerfile` & `PYTHONPATH`.
    - **Port Conflicts:** Ensure host port `8000` (or `HOST_API_PORT`) is free.
- **Tools Return Errors / Authentication Issues:**
    - **`401 Unauthorized` / `Cookie not found`:** Run the local login script (`python login.py`) again.
    - **Connection Error in MCP logs:** The `alexa_api` container is not running or not accessible from the MCP server.
- **Local Login Script (`login.py` at root) Errors:**
    - **WebDriver Errors:** Ensure Google Chrome is installed/updated locally.
    - **Cookie Extraction Failure:** Complete the browser login fully before pressing Enter.
    - **API Connection Error:** Verify `alexa_api` container is running and accessible at `http://localhost:8000` (or configured `API_PORT`). Check container logs (`docker compose logs alexa_api`).
    - **API 4xx/5xx Errors during upload:** Check `alexa_api` container logs for details.
