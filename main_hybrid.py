"""
Hybrid Approach: FastMCP-style tools + dedalus-mcp server
==========================================================

This uses dedalus-mcp framework (which works on Dedalus deployment)
but with the same simple decorator syntax that FastMCP offers.

The goal: Get the best of both worlds!
"""

import asyncio
from dedalus_mcp import MCPServer, tool


# Define tools using dedalus-mcp @tool decorator
# (Similar syntax to FastMCP)
@tool(description="Add two numbers together")
def add(a: int, b: int) -> int:
    """Add two numbers and return the result."""
    return a + b


@tool(description="Subtract second number from first")
def subtract(a: int, b: int) -> int:
    """Subtract b from a and return the result."""
    return a - b


@tool(description="Multiply two numbers")
def multiply(a: int, b: int) -> int:
    """Multiply two numbers and return the result."""
    return a * b


@tool(description="Divide first number by second")
def divide(a: float, b: float) -> float:
    """Divide a by b and return the result."""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


async def main():
    """Create server and register tools - dedalus-mcp style."""
    # Create dedalus-mcp server
    server = MCPServer("calculator-hybrid")

    # Collect all tools
    server.collect(add, subtract, multiply, divide)

    # Start server with dedalus-mcp's serve() method
    # This is what Dedalus deployment infrastructure expects!
    await server.serve(port=8000)


if __name__ == "__main__":
    print("Starting Hybrid Calculator Server (dedalus-mcp compatible)...")
    print("Using dedalus-mcp @tool decorators (FastMCP-style syntax)")
    asyncio.run(main())
