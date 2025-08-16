from typing_extensions import TypedDict
from pydantic import BaseModel, Field
from typing import Literal
from langchain_core.messages import HumanMessage, SystemMessage

from src.config.config import TAILOR_SYSTEM_PROMPT, DECISION_SYSTEM_PROMPT

class State(TypedDict):
    input : str
    decision : str
    output : str
    
class RouteDecision(BaseModel):
    step : Literal["Q&A", "LatestInfo", "Image", "PlatformContent"] = Field(description="The next step in the routing process.")


class Node:
    
    def __init__(self):
        pass 
    
    # Node 1
    def q_and_a(self,state : State, llm): # Done
        """Q&A"""
        result = llm.invoke(state["input"])
        return {"output" : result.content}

    # Node 2
    async def latest_info(self,state : State, search): # Done
        search_response = await search.ainvoke(
            {"messages" : [{"role" : "user", "content" : state["input"]}]}
        )
        return {"output" : search_response["messages"]}
        

    # Node 3
    def img_gen(self,state : State, agent): # Done
        img_url = agent.image_generation(state["input"])
        return {"output" : img_url}

    # Node 4
    def content_tailor(self, state : State, llm):
        result = llm.invoke(
            [
                SystemMessage(content=TAILOR_SYSTEM_PROMPT),
                HumanMessage(content=state["input"])
            ]
        )
        return {"output" : result.content}

    # Node 5
    def call_router(self, state : State, llm_with_decision):
        """Route the input to the appropriate node"""
        
        decision = llm_with_decision.invoke(
            [
                SystemMessage(
                    content=DECISION_SYSTEM_PROMPT
                ),
                HumanMessage(content=state["input"])
            ]
        )
        return {"decision" : decision.step}    
    
    # conditional function to route the node
    def route_decision(self, state : State):
        if state["decision"] == "Q&A":
            return "q_and_a"
        elif state["decision"] == "LatestInfo":
            return "latest_info"
        elif state["decision"] == "Image":
            return "img_gen"
        elif state["decision"] == "PlatformContent":
            return "content_tailor"
        else:
            return "q_and_a"