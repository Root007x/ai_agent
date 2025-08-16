from src.components.graph import build_agent
import asyncio
import unicodedata

from src.utils.custom_exception import CustomException
from src.utils.logger import logger

logger = logger(__name__)

async def main(query : str):
    try:
        graph = await build_agent()
        
        result = await graph.ainvoke(
            {
                "input": query
            }
        )
        
        return result
    
    except Exception as e:
        error = CustomException("An error occurred",e)
        logger.error(error)
        
if __name__ == "__main__":
    prompt = "Today BD temperature"
    output = asyncio.run(main(query=prompt))
    normalized_text = unicodedata.normalize('NFC', output["output"])
    print(normalized_text)