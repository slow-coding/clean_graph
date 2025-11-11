from typing import TypedDict, Annotated
from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages
from langchain_core.messages import BaseMessage, SystemMessage
from typing import Annotated, List
from .llms import llm


class State(TypedDict):
    messages: Annotated[List[BaseMessage], add_messages]


def agent(state: State) -> State:
    system_prompt = "You are a helpful assistant."
    messages = [SystemMessage(content=system_prompt)] + state["messages"]
    response = llm.invoke(messages)
    return {"messages": [response]}


def create_graph():
    graph = StateGraph(State)
    graph.add_node("agent", agent)
    graph.add_edge(START, "agent")
    return graph.compile()


app = create_graph()
