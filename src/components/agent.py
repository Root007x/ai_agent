from urllib.parse import quote
from langgraph.prebuilt import create_react_agent

from src.utils.logger import logger
from src.utils.custom_exception import CustomException

logger = logger(__name__)

class Agent:
    def __init__(self):
        pass 
    
    
    def image_generation(self, prompt : str):
        try:
            encoded_prompt = quote(prompt)
            image_url = f"https://image.pollinations.ai/prompt/{encoded_prompt}"
            
            logger.info("Image Generated Successfully")
            return image_url
        except Exception as e:
            error = CustomException("Failed To Generate Image",e)
            logger.error(str(error))
    
    def search_agent(self,agent_model, mcp_tools):
        search = create_react_agent(
            model=agent_model,
            tools=mcp_tools
        )
        logger.info("Search Agent Created Successfully")
        return search