from typing import List, Sequence, Literal
from dotenv import load_dotenv
from langchain_core.messages import BaseMessage, HumanMessage
from langgraph.graph import END, MessageGraph
from chains import generation_chain, reflection_chain

load_dotenv()

REFLECT = "reflect"
GENERATE = "generate"
graph = MessageGraph()

def generate_node(state):
    return generation_chain.invoke({
        "messages": state
    })


def reflect_node(messages):
    # print("The messages for reflect node - ", messages)
    response = reflection_chain.invoke({
        "messages": messages
    })
    # print("From reflection AI got - ", response)
    return [HumanMessage(content=response.content)]


graph.add_node(GENERATE, generate_node)
graph.add_node(REFLECT, reflect_node)
graph.set_entry_point(GENERATE)


def should_continue(state) -> Literal["REFLECT", "END"]:
    if (len(state) > 2):
        return END 
    return REFLECT


graph.add_conditional_edges(GENERATE, 
        should_continue, 
        path_map={
        REFLECT: REFLECT,
        END: END
    })
graph.add_edge(REFLECT, GENERATE)

app = graph.compile()

print(app.get_graph().draw_mermaid())
# app.get_graph().print_ascii()

response = app.invoke(HumanMessage(content="AI Agents taking over content creation"))

print(response[-1])

# import pdb; pdb.set_trace()
# reflection_chain.invoke("This is my tweet: I am amazing how are you all doing today")