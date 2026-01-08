#!/bin/bash

# Activate virtual environment and run the Amazon login script
cd "$(dirname "$0")"
source .venv/bin/activate
python -m src.auth.login

# Check if login was successful
if [ $? -eq 0 ]; then
    echo ""
    echo "✅ Authentication successful!"
    echo "Testing connection to shopping list..."
    echo ""

    # Give the API a moment to process the cookies
    sleep 2

    # Test the API connection
    response=$(curl -s http://localhost:8092/)
    if [[ $response == *"Alexa Shopping List API"* ]]; then
        echo "✅ Shopping list API is responding correctly"
        echo "You can now use the add_shopping_item tool!"
    else
        echo "⚠️  API may not be running. Check with: docker compose ps"
    fi
else
    echo ""
    echo "❌ Authentication failed. Please try again."
    exit 1
fi
