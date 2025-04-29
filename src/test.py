from langchain_ollama import ChatOllama
from langchain_core.messages import AIMessage
from logging import getLogger
logger = getLogger(__file__)
llm = ChatOllama(
    model="gemma3:4b-it-q4_K_M",
    temperature=0.5,
)
messages = [
    (
        "system",
        "You are a helpful assistant",
    ),
    ("human", "Write me a short poem about a cat."),
]
ai_msg = llm.invoke(messages)
print(ai_msg.content)