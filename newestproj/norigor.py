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



search = SerpAPIWrapper()

tools = [

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
    #     Tool(
    #     name = "OCR Understanding",
    #     func=imun_read.run,
    #     description=(
    #     "A wrapper around OCR Understanding (Optical Character Recognition). "
    #     "Useful after Image Understanding tool has found text or handwriting is present in the image tags."
    #     "This tool can find the actual text, written name, or product name in the image."
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
llm = ChatOpenAI(temperature=0)
memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
agent_chain = initialize_agent(tools, llm, agent="chat-conversational-react-description", verbose=True, memory=memory)


# agent_chain.run("what are some good dinners to make this week, if i like thai food?")

agent_chain.run(input="who is Madison Davis")
