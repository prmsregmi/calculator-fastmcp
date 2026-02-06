"""
Simple Calculator MCP - Built with FastMCP
===========================================

A minimal MCP server using FastMCP with SSE transport.

To run locally:
    python main.py

Server will run at: http://127.0.0.1:8000/mcp

To deploy to Dedalus:
    1. Push this folder to GitHub
    2. Go to https://dedaluslabs.ai/dashboard
    3. Click "Add Server"
    4. Connect your repo
    5. Deploy
"""

from mcp.server.fastmcp import FastMCP

# Create FastMCP server with SSE transport
mcp = FastMCP("calculator-fast", transport="sse")


@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers together."""
    return a + b


@mcp.tool()
def subtract(a: int, b: int) -> int:
    """Subtract second number from first."""
    return a - b


@mcp.tool()
def multiply(a: int, b: int) -> int:
    """Multiply two numbers."""
    return a * b


@mcp.tool()
def divide(a: float, b: float) -> float:
    """Divide first number by second."""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


if __name__ == "__main__":
    print("Starting FastMCP Calculator Server...")
    print("Server running at: http://127.0.0.1:8000/mcp")
    mcp.run(transport="sse", host="0.0.0.0", port=8000, path="/mcp")
