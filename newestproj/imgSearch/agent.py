from langchain.chat_models import ChatOpenAI
from langchain.agents import initialize_agent
from langchain.agents import Tool
from langchain.utilities import SerpAPIWrapper
from langchain.memory import ConversationBufferMemory
import imgSearch

tools = [
    Tool(
        name="Item Identification",
        func=imgSearch.imgSearch,
        description="Useful when you want to identify an object"
    ),
]

llm = ChatOpenAI(temperature=0)
memory = ConversationBufferMemory(
    memory_key="chat_history", return_messages=True)
agent_chain = initialize_agent(
    tools, llm, agent="chat-conversational-react-description", verbose=True, memory=memory)

while True:
    print("AI: " + agent_chain.run(input=input("Human: ")))
