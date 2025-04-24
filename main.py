## BEGIN IMPORT MODULES
import os
from functools import partial
from langgraph.graph import StateGraph, START, END
from langchain_anthropic import ChatAnthropic
## from IPython.display import Image, display
from dotenv import load_dotenv
import mod_cls_0_CreateStateClassObject
import mod_0_CreateAgent
import mod_1_StreamGraphUpdates

## LOAD THE ENVIRONMENT VARIABLE FOR SECURE API KEY ACCESS
load_dotenv() ## BOOLEAN

## DEFINE VARIABLES
API_KEY_ANTHROPIC = os.getenv("API_KEY_ANTHROPIC") ## ACCESS API SECURELY: LOAD ENVIRONMENT VARIABLES FROM .env FILE 
MODEL = "claude-3-5-sonnet-20240620"
State = mod_cls_0_CreateStateClassObject.State 

## TEST PRINT OUTPUT
print(f"API Key loaded: {API_KEY_ANTHROPIC is not None}")
print(f"API Key first few chars: {API_KEY_ANTHROPIC[:10]}..." if API_KEY_ANTHROPIC else "API Key not found")
print(f"State: {State}")
print(f"type(State): {type(State)}")

## BEGIN MAIN PROGRAM
## CALL CLASS OBJECT
GraphBuilder = StateGraph(State)

## TEST PRINT OUTPUT
print(f"type(GraphBuilder): {type(GraphBuilder)}")

## CALL CLAUDE: OH, CLAUDE! COME HITHER, S'IL VOUS PLAIT
LLM = ChatAnthropic(api_key=API_KEY_ANTHROPIC, model=MODEL)

## TEST PRINT OUTPUT
print(f"type(LLM): {type(LLM)}")

## CALL MODULE.FUNCTION(): CREATE AGENT
## CREATE PARTIAL FUNCTION THAT LOCKS IN THE LLM, BUT LEAVES STATE TO BE PASSED LATER
## ChatbotNode = partial(state=State, llm=LLM)
ChatbotNode = partial(mod_0_CreateAgent.Chatbot, llm=LLM)

## CALL FUNCTION
## REGISTER NODE WITH THE GRAPH
GraphBuilder.add_node("chatbot", ChatbotNode)
GraphBuilder.add_node("ChatbotNode", ChatbotNode) ## (UNIQUE NODE NAME, FUNCTION OR OBJECT CALLED WHENEVER THE NODE IS USED)
GraphBuilder.add_edge(START, "ChatbotNode")
GraphBuilder.add_edge("ChatbotNode", END)
Graph = GraphBuilder.compile()

## TEST PRINT OUTPUT
print(f"type(Graph): {type(Graph)}")

## BEGIN WHILE GAME LOOP
while True:
    try:
        ## IF USER INPUT AVAILABLE
        user_input = input("User: ")
        if user_input.lower() in ["quit", "exit", "q"]:
            print("Goodbye!")
            break

        ## IF USER INPUT IS NOT QUIT / EXIT / Q AS ABOVE
        mod_1_StreamGraphUpdates.StreamGraphUpdates(user_input, Graph)

    except:
        ## ELSE IF USER INPUT NOT AVAILABLE
        user_input = "What do you know about LangGraph?"
        print("User: " + user_input)
        mod_1_StreamGraphUpdates.StreamGraphUpdates(user_input, Graph)
        break
## END WHILE GAME LOOP

## END MAIN PROGRAM
## GAME OVER

'''
## BEGIN DISPLAY IMAGE
try:
    pass ## display(Image(graph.get_graph().draw_mermaid_png())) # This requires some extra dependencies and is optional

except Exception:
    # This requires some extra dependencies and is optional
    pass

## END DISPLAY IMAGE
'''