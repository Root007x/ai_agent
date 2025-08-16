from langchain_mcp_adapters.client import MultiServerMCPClient
import asyncio

from src.config.config import TOOL_API
from src.utils.logger import logger
from src.utils.custom_exception import CustomException

logger = logger(__name__)


class ModelTools:
    
    def __init__(self):
        pass 
    
    # Search tool
    async def get_tools_async(self):
        try:
            client = MultiServerMCPClient({
                "server1": {
                    "url": TOOL_API,
                    "transport": "streamable_http",
                }
            })
                # Get tools from all servers
            tools = await client.get_tools()
                
            logger.info("Tools fetched successfully")
            return tools
        
        except Exception as e:
            error = CustomException("Failed to connect MCP server", e)
            logger.error(str(error))
        
    

    