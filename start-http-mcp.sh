#!/bin/bash
# Start HTTP MCP Server for Alexa Shopping List
# This server exposes the Alexa Shopping List API via HTTP endpoints
# compatible with myndy-brain's MCP client

set -e

PROJECT_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$PROJECT_ROOT"

echo "🚀 Starting Alexa Shopping List HTTP MCP Server..."
echo "📍 Project root: $PROJECT_ROOT"

# Check if virtual environment exists
if [ ! -d ".venv" ]; then
    echo "❌ Virtual environment not found at .venv"
    echo "Please run: uv venv && source .venv/bin/activate && uv pip install -r src/mcp/requirements.txt"
    exit 1
fi

# Activate virtual environment
echo "🔧 Activating virtual environment..."
source .venv/bin/activate

# Check if required dependencies are installed
if ! python -c "import fastapi, uvicorn, requests" 2>/dev/null; then
    echo "📦 Installing required dependencies..."
    pip install fastapi uvicorn requests pydantic
fi

# Check if API server is running
echo "🔍 Checking if Alexa API server is running..."
if ! curl -s http://localhost:8000/ > /dev/null 2>&1; then
    echo "⚠️  Warning: Alexa API server not responding at http://localhost:8000"
    echo "   Make sure to start it with: docker compose up -d alexa_api"
    echo ""
fi

# Start HTTP MCP server
echo "▶️  Starting HTTP MCP Server on port 8091..."
echo "   API Docs will be available at: http://localhost:8091/docs"
echo ""

python -m src.mcp.http_mcp_server
