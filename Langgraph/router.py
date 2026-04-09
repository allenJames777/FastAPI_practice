
#ROUTER ARCHITECTURE
#Conditional Logic 
#if someone needs help on math go to ROOM 1 
#if someone needs help on science go to ROOM 2
#if someone needs help on General go to Room 3
import os
os.environ["GROQ_API_KEY"] = "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"


from langchain_groq import ChatGroq
from langgraph.graph import StateGraph, START, END
from typing import TypedDict

#The goal: the AI decides which path to take based on your question.
#model To Use
llm = ChatGroq(model="llama-3.1-8b-instant")

#Create a pydantic model
class State(TypedDict):
    message: str
    category:str
    response:str

#Node1 Classify/Arrange the question
def classify(state: State):
    result = llm.invoke(f"Classify this question as 'math' or 'general'. Reply with one word only: {state['message']}")
    return{"category": result.content.strip().lower()}

#Node2: math answer
def math_response(state: State):
    result = llm.invoke(f"Solve this math problem{state['message']}")
    return{"response": result.content}

#Node3: general answer
def gen_response(state: State):
    result = llm.invoke(f"Answer this question: {state['message']}")
    return{"response": result.content}

#Router decision on where to go
def route(state: State):
    if "math" in state["category"]:
        return "math_response"
    return "gen_response"

#BUILDING THE GRAPH
#ADD NODES
graph = StateGraph(State)
graph.add_node("classify", classify)#("node name", function)
graph.add_node("math_response", math_response)#("node name", function)
graph.add_node("gen_response", gen_response)#("node name", function)

#ADD EDGE 
graph.add_edge(START,"classify")
graph.add_conditional_edges("classify", route)
graph.add_edge("math_response", END)
graph.add_edge("gen_response", END)

#final step compile everything
app = graph.compile()

#final step for input and output via CLI 
while True:
    user_input = input("You:")
    if user_input == "quit":
        break
    result = app.invoke({"message":user_input})
    print(f"Category: {result['category']}")
    print(f"AI: {result['response']}")