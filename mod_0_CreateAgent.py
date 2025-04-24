## IMPORT MODULES
from langchain_anthropic import ChatAnthropic
from mod_cls_0_CreateStateClassObject import State

## BEGIN DEFINE FUNCTION
def Chatbot(state: State, llm: ChatAnthropic):

    """ 
    Create a chatbot node function that properly handles message types.
    
    Args:
        state: The current state object containing messages
        llm: The ChatAnthropic language model
        
    Returns:
        A dictionary with updated messages
    
    ## FROM LANGCHAIN DOCS: Notice how the chatbot node function takes the current State as input and returns a dictionary containing
    an updated messages list under the key "messages". This is the basic pattern for all LangGraph node functions.
    """

    ## RETURN OLD FROM LANGCHAIN DOCS:
    return {"messages": [llm.invoke(state["messages"])]}

## END DEFINE FUNCTION


