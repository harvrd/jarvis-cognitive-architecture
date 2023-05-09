from langchain.chat_models import ChatOpenAI
from langchain.agents import initialize_agent
from langchain.agents import Tool
from langchain.utilities import SerpAPIWrapper
from langchain.memory import ConversationBufferMemory
# import imunCool
import imgSearch


search = SerpAPIWrapper()

tools = [
    # Tool(
    #     name="Get Image Details",
    #     func=imunCool.DenseCaptioning,
    #     description=(
    #         "A wrapper around Image Understanding. "
    #         "Useful for when you need to understand what is inside an image (objects, texts, people)."
    #         "Input should be an image url, or path to an image file (e.g. .jpg, .png)."
    #     )
    # ),
    Tool(
        name="Reverse Image Search",
        func=imgSearch.imgSearch,
        description="Useful when you want to answer questions about the context of an image"
    ),
    Tool(
        name="Search",
        func=search.run,
        description="Useful when you want to answer questions about current events or things found online"
    )
]

llm = ChatOpenAI(temperature=0)
memory = ConversationBufferMemory(
    memory_key="chat_history", return_messages=True)
agent_chain = initialize_agent(
    tools, llm, agent="chat-conversational-react-description", verbose=True, memory=memory)

while True:
    print("AI: " + agent_chain.run(input=input("Human: ")))
# agent_chain.run(input="what's the brand of this soda: /Users/yutongwu/Documents/GitHub/jarvis-cognitive-architecture/newestproj/cola.png")
