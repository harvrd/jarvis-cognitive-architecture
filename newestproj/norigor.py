from langchain.prompts import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.agents import initialize_agent
from langchain.agents import Tool
from langchain.prompts.chat import (
    ChatPromptTemplate,
    HumanMessagePromptTemplate,
)
from langchain.utilities import SerpAPIWrapper
from langchain.memory import ConversationBufferMemory
import imunCool



search = SerpAPIWrapper(serpapi_api_key = '1bcb3681fc3084e00e53558d117b152f7102db70869b3afe3f8c5639ac352551')

tools = [
    Tool(
        name = "Get Image Details",
        func=imunCool.DenseCaptioning,
        description=(
        "A wrapper around Image Understanding. "
        "Useful for when you need to understand what is inside an image (objects, texts, people)."
        "Input should be an image url, or path to an image file (e.g. .jpg, .png)."
        )
    ),
    # Tool(
    #     name = "Layout Understanding",
    #     func=imun_layout.run,
    #     description=(
    #     "A wrapper around layout and table understanding. "
    #     "Useful after Image Understanding tool has recognized businesscard in the image tags."
    #     "This tool can find the actual business card text, name, address, email, website on the card."
    #     "Input should be an image url, or path to an image file (e.g. .jpg, .png)."
    #     )
    # ),      
    Tool(
        name = "search",
        func=search.run,
        description="Useful when you want to answer questions about current events or things found online"
    )
]

# human_message_prompt = HumanMessagePromptTemplate(
#         prompt=PromptTemplate(
#             template="You are JARVIS, a personal assistant for Yutong Wu.",
#             input_variables=["product"],
#         )
#     )
# chat_prompt_template = ChatPromptTemplate.from_messages([human_message_prompt])
llm = ChatOpenAI(temperature=0, openai_api_key='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')
memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
agent_chain = initialize_agent(tools, llm, agent="chat-conversational-react-description", verbose=True, memory=memory)


# agent_chain.run("what are some good dinners to make this week, if i like thai food?")

while True:
    print("AI: " + agent_chain.run(input=input("Human: ")))
# agent_chain.run(input="what's the brand of this soda: /Users/yutongwu/Documents/GitHub/jarvis-cognitive-architecture/newestproj/cola.png")