## BEGIN IMPORT MODULES
import os
from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages
from langchain_anthropic import ChatAnthropic
from typing import Annotated
from typing_extensions import TypedDict
## from IPython.display import Image, display
from dotenv import load_dotenv 

## LOAD THE ENVIRONMENT VARIABLE FOR SECURE API KEY ACCESS
load_dotenv() ## BOOLEAN

## DEFINE VARIABLES
API_KEY_ANTHROPIC = os.getenv("API_KEY_ANTHROPIC") ## ACCESS API SECURELY: LOAD ENVIRONMENT VARIABLES FROM .env FILE 
MODEL = "claude-3-5-sonnet-20240620"

## TEST PRINT OUTPUT
print(f"API Key loaded: {API_KEY_ANTHROPIC is not None}")
print(f"API Key first few chars: {API_KEY_ANTHROPIC[:10]}..." if API_KEY_ANTHROPIC else "API Key not found")

## BEGIN DEFINE CLASS OBJECT
class State(TypedDict):
    # Messages have the type "list". The `add_messages` function
    # in the annotation defines how this state key should be updated
    # (in this case, it appends messages to the list, rather than overwriting them)
    messages: Annotated[list, add_messages]

## END DEFINE CLASS OBJECT

## BEGIN DEFINE FUNCTION
def Chatbot(state: State):

    """ Notice how the chatbot node function takes the current State as input and returns a dictionary containing
    an updated messages list under the key "messages". This is the basic pattern for all LangGraph node functions."""

    ## RETURN
    return {"messages": [llm.invoke(state["messages"])]}

## END DEFINE FUNCTION

## BEGIN MAIN PROGRAM

## CALL CLASS OBJECT
GraphBuilder = StateGraph(State)

## CALL CLAUDE: OH, CLAUDE! DO MY BIDDING, S'IL VOUS PLAIT
llm = ChatAnthropic(api_key=API_KEY_ANTHROPIC, model=MODEL)

## CALL FUNCTION
GraphBuilder.add_node("chatbot", Chatbot) ## (UNIQUE NODE NAME, FUNCTION OR OBJECT CALLED WHENEVER THE NODE IS USED)
GraphBuilder.add_edge(START, "chatbot")
GraphBuilder.add_edge("chatbot", END)
graph = GraphBuilder.compile()

## BEGIN DEFINE FUNCTION
def StreamGraphUpdates(user_input: str):
    for event in graph.stream({"messages": [{"role": "user", "content": user_input}]}):
        for value in event.values():
            print("Assistant:", value["messages"][-1].content)

## END DEFINE FUNCTION

## END MAIN PROGRAM
## GAME OVER

"""
## BEGIN WHILE LOOP
while True:
    try:
        user_input = input("User: ")
        if user_input.lower() in ["quit", "exit", "q"]:
            print("Goodbye!")
            break
        StreamGraphUpdates(user_input)
    except:
        # fallback if input() is not available
        user_input = "What do you know about LangGraph?"
        print("User: " + user_input)
        StreamGraphUpdates(user_input)
        break
## END WHILE LOOP
"""

## BEGIN DISPLAY IMAGE
try:
    pass ## display(Image(graph.get_graph().draw_mermaid_png())) # This requires some extra dependencies and is optional

except Exception:
    # This requires some extra dependencies and is optional
    pass

## END DISPLAY IMAGE
