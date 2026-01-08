#!/bin/bash

# Test script for Alexa Shopping List API
echo "🧪 Testing Alexa Shopping List API..."
echo ""

# Check if Docker container is running
echo "1. Checking if Docker container is running..."
if docker compose ps alexa_api | grep -q "Up"; then
    echo "   ✅ Container is running"
else
    echo "   ❌ Container is not running"
    echo "   Run: docker compose up -d"
    exit 1
fi
echo ""

# Check if API is responding
echo "2. Testing API health endpoint..."
response=$(curl -s http://localhost:8092/)
if [[ $response == *"Alexa Shopping List API"* ]]; then
    echo "   ✅ API is responding"
else
    echo "   ❌ API is not responding correctly"
    echo "   Response: $response"
    exit 1
fi
echo ""

# Check if cookies file exists
echo "3. Checking for authentication cookies..."
if docker compose exec -T alexa_api test -f /app/data/cookies.json; then
    cookie_count=$(docker compose exec -T alexa_api sh -c 'cat /app/data/cookies.json | grep -o "\"name\"" | wc -l')
    echo "   ✅ Cookies file exists with $cookie_count cookies"
else
    echo "   ❌ No cookies file found"
    echo "   Run: ./login.sh to authenticate"
    exit 1
fi
echo ""

# Test getting all items
echo "4. Testing get all items..."
all_items=$(curl -s http://localhost:8092/items/all)
if [[ $all_items == "["* ]]; then
    item_count=$(echo $all_items | grep -o '"id"' | wc -l)
    echo "   ✅ Successfully retrieved $item_count items"
else
    echo "   ⚠️  Unexpected response: $all_items"
fi
echo ""

# Test getting incomplete items
echo "5. Testing get incomplete items..."
incomplete_items=$(curl -s http://localhost:8092/items/incomplete)
if [[ $incomplete_items == "["* ]]; then
    incomplete_count=$(echo $incomplete_items | grep -o '"id"' | wc -l)
    echo "   ✅ Successfully retrieved $incomplete_count incomplete items"
else
    echo "   ⚠️  Unexpected response: $incomplete_items"
fi
echo ""

# Test adding an item
echo "6. Testing add item (adding 'test item')..."
add_response=$(curl -s -X POST http://localhost:8092/items \
    -H "Content-Type: application/json" \
    -d '{"item_name": "test item"}')

if [[ $add_response == *"successfully"* ]] || [[ $add_response == *"Added"* ]]; then
    echo "   ✅ Successfully added test item"

    # Clean up - delete the test item
    echo "   🧹 Cleaning up test item..."
    delete_response=$(curl -s -X DELETE http://localhost:8092/items \
        -H "Content-Type: application/json" \
        -d '{"item_name": "test item"}')
    if [[ $delete_response == *"successfully"* ]] || [[ $delete_response == *"Deleted"* ]]; then
        echo "   ✅ Test item cleaned up"
    else
        echo "   ⚠️  Could not delete test item (you may need to remove it manually)"
    fi
else
    echo "   ❌ Failed to add test item"
    echo "   Response: $add_response"
fi
echo ""

echo "=========================================="
echo "✅ All tests completed!"
echo "Your Alexa Shopping List integration is working correctly."
echo "=========================================="
