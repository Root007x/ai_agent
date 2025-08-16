from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.responses import JSONResponse
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



app = FastAPI()

class Request(BaseModel):
    task : str



@app.get("/")
def home():
    return {"messages" : "I am FastAPI"}


@app.post("/task")
async def task(request : Request):
    
    query = request.task
    result = await main(query=query)
    output = result.get("output", "") if result else ""
    normalize_output = unicodedata.normalize('NFC', output)
    
    try:
        return JSONResponse(
            status_code=200,
            content={
                "response" : normalize_output
            }
        )
    except Exception as e:
        return JSONResponse(status_code=200, content=str(e))
