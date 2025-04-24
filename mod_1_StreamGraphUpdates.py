## IMPORT MODULES

## BEGIN DEFINE FUNCTION
def StreamGraphUpdates(user_input: str, Graph):
    for event in Graph.stream({"messages": [{"role": "user", "content": user_input}]}):
        for value in event.values():
            print("Assistant:", value["messages"][-1].content)

## END DEFINE FUNCTION