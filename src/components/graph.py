from langgraph.graph import StateGraph, START, END
from functools import partial


from src.components.model import LLMModel
from src.components.tools import ModelTools
from src.components.agent import Agent
from src.components.node import Node, State, RouteDecision


async def build_agent(): 
    ## Init model
    llm = LLMModel()
    ## Init Tools
    tools = ModelTools()
    # Init Agent
    agent = Agent()


    # Model Load
    general_llm = llm.decision_model()
    search_llm = llm.agent_model()

    # Tools
    mcp_tools = await tools.get_tools_async()

    # Search agent
    search_agent = agent.search_agent(search_llm, mcp_tools)

    # LLM with decision
    llm_with_decision = general_llm.with_structured_output(RouteDecision)

    # Node Init
    state_node = Node()
    node_1 = partial(state_node.q_and_a, llm=general_llm)
    node_2 = partial(state_node.latest_info, search=search_agent)
    node_3 = partial(state_node.img_gen, agent=agent)
    node_4 = partial(state_node.content_tailor, llm=general_llm)
    node_5 = partial(state_node.call_router, llm_with_decision=llm_with_decision)


    # Graph Build
    graph_builder = StateGraph(State)

    # Add Node
    graph_builder.add_node("call_router", node_5)
    graph_builder.add_node("q_and_a", node_1)
    graph_builder.add_node("latest_info", node_2)
    graph_builder.add_node("img_gen", node_3)
    graph_builder.add_node("content_tailor", node_4)

    # Add edge
    graph_builder.add_edge(START, "call_router")
    graph_builder.add_conditional_edges(
        "call_router",
        state_node.route_decision,
        {
            "q_and_a" : "q_and_a",
            "latest_info" : "latest_info",
            "img_gen" : "img_gen",
            "content_tailor" : "content_tailor"
        }
    )

    graph_builder.add_edge("q_and_a", END)
    graph_builder.add_edge("img_gen", END)
    graph_builder.add_edge("content_tailor", END)
    graph_builder.add_edge("latest_info", END)

    return graph_builder.compile()









