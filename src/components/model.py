from langchain_groq import ChatGroq

from src.config.config import GROQ_API_KEY, LLM_MODEL_NAME, LLM_AGENT_MODEL_NAME
from src.utils.logger import logger
from src.utils.custom_exception import CustomException


logger = logger(__name__)


class LLMModel:
    
    def __init__(self):
        pass 
    
    
    def decision_model(self):
        try:
            llm = ChatGroq(
                    model= LLM_MODEL_NAME,
                    api_key=GROQ_API_KEY
                )
            logger.info("Decision LLM Model Initialize successfully")
            return llm
        except Exception as e:
            error = CustomException("Failed to connect with LLM model")
            logger.error(str(error))
    
    def agent_model(self):
        try:
            llm = ChatGroq(
                    model= LLM_AGENT_MODEL_NAME,
                    api_key=GROQ_API_KEY
                )
            logger.info("Agent LLM Model Initialize successfully")
            return llm
        except Exception as e:
            error = CustomException("Failed to connect with LLM model 2", e)
            logger.error(str(error))
    