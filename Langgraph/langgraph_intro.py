import os
from dotenv import load_dotenv
load_dotenv()

from langchain_groq import ChatGroq
from langgraph.graph import StateGraph, START, END
from typing import TypedDict

class State(TypedDict):
    message: str
    response: str

def chat(state: State):
    llm = ChatGroq(model="llama-3.1-8b-instant")
    result = llm.invoke(state["message"])
    return {"response": result.content}

graph = StateGraph(State)
graph.add_node("chat", chat)
graph.add_edge(START, "chat")
graph.add_edge("chat", END)

app = graph.compile()

while True:
    user_input = input("You: ")
    if user_input == "quit":
        break
    result = app.invoke({"message": user_input})
    print(f"AI: {result['response']}")