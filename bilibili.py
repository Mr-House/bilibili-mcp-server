from mcp.server.fastmcp import FastMCP
from bilibili_api import search, sync

mcp = FastMCP()

@mcp.tool()
def general_search(keyword: str) -> dict: 
    """
    Search Bilibili API with the given keyword.

    Args:
        keyword (str): Search term to look for on Bilibili.

    Returns:
        dict: Dictionary contains the search results from Bilibili.
    """
    return sync(search.search(keyword))


if __name__ == "__main__":
    mcp.run(transport="stdio")
