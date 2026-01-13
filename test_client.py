import asyncio
from fastmcp import Client


async def main():
    # Point the client at your server file (stdio transport)
    # client = Client("my_server.py")

    # Connect to the HTTP server
    client = Client("http://localhost:8000")

    # Connect to the server
    async with client:
        # List available tools
        tools = await client.list_tools()
        print("Available tools:")
        for tool in tools:
            print(f"  - {tool.name}: {tool.description}")

        print("\n" + "=" * 50 + "\n")

        # Call the weather tool
        result = await client.call_tool(
            "get_weather",
            {"city": "Tokyo"}
        )
        print(f"Weather result: {result}")


if __name__ == "__main__":
    asyncio.run(main())