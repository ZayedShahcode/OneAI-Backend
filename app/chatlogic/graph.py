from typing import Sequence

from langchain_core.messages import BaseMessage, trim_messages
from langgraph.graph.message import add_messages
from typing_extensions import Annotated, TypedDict
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langgraph.checkpoint.memory import MemorySaver
from langgraph.graph import START, StateGraph
from langchain_core.prompts import ChatPromptTemplate,MessagesPlaceholder

load_dotenv()
model = init_chat_model("llama-3.1-8b-instant", model_provider="groq")

prompt_template = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are a  helpful assistant",
        ),
        MessagesPlaceholder(variable_name="messages"),
    ]
)

trimmer = trim_messages(
    max_tokens=300,
    strategy="last",
    token_counter = model,
    include_system=True,
    allow_partial=False,
    start_on="human",
)

class State(TypedDict):
    messages: Annotated[Sequence[BaseMessage], add_messages]
    # language: str

workflow = StateGraph(state_schema=State)

async def call_model(state: State):
    trimmed_messages = await trimmer.ainvoke(state["messages"])
    prompt = await prompt_template.ainvoke(
        {"messages": trimmed_messages},
    )
    response = await model.ainvoke(prompt)
    return {"messages": [response]}

workflow.add_edge(START, "model")
workflow.add_node("model", call_model)

memory = MemorySaver()
bot = workflow.compile(checkpointer=memory)