# minimal_test_server.py
from fastmcp import FastMCP

mcp = FastMCP("Minimal Demo 🚀")

@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b

if __name__ == "__main__":
    # Add some print statements for debugging, similar to our previous attempts
    import sys
    print("--- Minimal Test Server: Starting run() ---", file=sys.stderr); sys.stderr.flush()
    try:
        mcp.run()
    except Exception as e:
        print(f"--- Minimal Test Server FATAL ERROR: {e} ---", file=sys.stderr); sys.stderr.flush()
        import traceback
        traceback.print_exc(file=sys.stderr)
        sys.exit(1)
    finally:
        print("--- Minimal Test Server: run() finished ---", file=sys.stderr); sys.stderr.flush()
