# Calculator MCP - FastMCP

Built with **FastMCP** - the fast, Pythonic way to build MCP servers.

## Setup

```bash
pip install fastmcp
```

## Run Locally

```bash
python main.py
```

Server uses stdio transport by default.

## Deploy to Dedalus

1. Push this folder to GitHub repo
2. Go to https://dedaluslabs.ai/dashboard
3. Click "Add Server"
4. Connect your GitHub repo
5. Click "Deploy"

## Tools Provided

- `add(a, b)` - Add two numbers
- `subtract(a, b)` - Subtract b from a
- `multiply(a, b)` - Multiply two numbers
- `divide(a, b)` - Divide a by b

## Framework

This uses **FastMCP**:
- Most popular MCP framework (70% of all MCP servers use it)
- Decorator-based, Pythonic API
- Automatic schema generation from type hints
- Fast and minimal boilerplate
- Powers 1M+ downloads per day
