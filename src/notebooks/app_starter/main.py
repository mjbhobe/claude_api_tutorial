from mcp.server.fastmcp import FastMCP
from src.notebooks.app_starter.tools.math import add
from src.notebooks.app_starter.tools.document import document_path_to_markdown

mcp = FastMCP("docs")

mcp.tool()(add)
mcp.tool()(document_path_to_markdown)

if __name__ == "__main__":
    mcp.run()
