# script that has a general agent that can use tools necessary for the prompt.

from langchain import OpenAI, LLMChain,OpenAIChat
from langchain.agents import initialize_agent, ZeroShotAgent, tool, AgentExecutor, Tool, load_tools
from langchain.prompts import PromptTemplate
from langchain.chains.conversation.memory import ConversationBufferMemory
from langchain.chains import VectorDBQAWithSourcesChain
from langchain.utilities import SerpAPIWrapper
import faiss
import pickle
import os
from dotenv import load_dotenv

load_dotenv()

os.environ["OPENAI_API_KEY"] = os.getenv('OPENAI_API_KEY')
os.environ['SERPAPI_API_KEY'] = os.getenv('SERPAPI_API_KEY')

# Load vector store object
index = faiss.read_index("docs.index")
with open("faiss_store.pkl", "rb") as f:
    store = pickle.load(f)
store.index = index

# # Pre-processing of the prompt
# CV_caption = "a yellow Labrador retriever playing with a red ball in a grassy field." ## Sample caption, need to be replaced later
# NLP_caption = "what kind of dog is that, what do you think." ## Sample caption, need to be replaced later
# llm = OpenAI(temperature=0.9)
# prompt = PromptTemplate(
#     input_variables=["CV_caption","NLP_caption"],
#     template= """The CV caption is: {CV_caption} 
#                            The NLP caption is: {NLP_caption} 
#                            summarize this two prompt in the format The user is asking for _____ of ______. 
#                            Finally transform the summary into one or multiple of the the question templates 
#                            ["What is the ____ of the ____?", "Why _____ [verb]?, "How could ______ [verb]?"]
#                             ,and answer it with more details. format of summary is: Question: _____ Answer:_____"""
# )
# chain = LLMChain(llm=llm, prompt=prompt)
# # Run the chain only specifying the input variable.
# ans = chain.run({"CV_caption":CV_caption,"NLP_caption":NLP_caption})
# print(ans)

@tool
def documentation(query: str) -> str:
    """Searches the API for the query."""
    chain = VectorDBQAWithSourcesChain.from_llm(llm=OpenAI(temperature=0), vectorstore=store)
    result = chain({"question": query})
    return (f"Answer: {result['answer']} Sources: {result['sources']}")

@tool
def chat(text: str) -> str:
    """Uses ChatGPT to generate a response to the input text."""
    gpt3 = OpenAI(model_name="text-davinci-002", n=2, best_of=2)
    result = gpt3.generate(["Tell me a joke", "Tell me a poem"]*15)
    return result.generations

# define tools
search = SerpAPIWrapper()

tools = [
    Tool(
        name = "Current Search",
        func=search.run,
        description="useful for when you need to answer questions about current events or the current state of the world"
    ),
    Tool(
        name = "Documentation",
        func= lambda query: documentation(query),
        description="useful for when you need to answer questions about AtomXR or CaineScript documentation, and general questions about AtomXR. Also good for asking about syntax of functions and methods.",
        return_direct=True
    ),
    Tool(
        name = "Chat",
        func= lambda text: chat(text),
        description="uses ChatGPT to generate a response to the input text",
        return_direct=True
    )
]

# separate episodic vs semantic memory:
"""
episodic memory = events (day by day happenings, memories from chat)
semantic memory = not tied to specific experience (people's emails, birthdays, etc)
"""

memory_tools = [
    Tool(
        name = "AddEpisodicMemory",
        func= lambda memory: add_episodic_memory(memory),
        description="useful for when you are adding specific memories or events",
        return_direct=True
    ),
    Tool(
        name = "AddSemanticMemory",
        func= lambda memory: add_episodic_memory(memory),
        description="useful for when you are adding general knowledge or facts not tied to specific events",
        return_direct=True
    ),
    Tool(
        name = "Chat",
        func= lambda text: chat(text),
        description="uses ChatGPT to generate a response to the input text",
        return_direct=True
    )
]

# long term memory updating agent
@tool
def add_episodic_memory(memory):
    with open('episodic_memory.txt', 'a') as file:
        file.write(memory + '\n')    
    pass

@tool
def add_semantic_memory(memory):
    with open('semantic_memory.txt', 'a') as file:
        file.write(memory + '\n')    
    pass

def update_memory(memory):
    # find memory
    pass
# if appending memory
    # append memory
# else:
    # if memory exists:
        # update memory
    # else:
        # append memory




prefix = """Have a conversation with a human, answering the following questions as best you can. You have access to the following tools:"""
suffix = """Begin!"

{chat_history}
Question: {input}
{agent_scratchpad}"""

prompt = ZeroShotAgent.create_prompt(
    tools, 
    prefix=prefix, 
    suffix=suffix, 
    input_variables=["input", "chat_history", "agent_scratchpad"]
)
memory = ConversationBufferMemory(memory_key="chat_history")

llm_chain = LLMChain(llm=OpenAI(temperature=0), prompt=prompt)
agent = ZeroShotAgent(llm_chain=llm_chain, tools=tools, verbose=True)
agent_chain = AgentExecutor.from_agent_and_tools(agent=agent, tools=tools, verbose=True, memory=memory)

while True:
    print("AI: " + agent_chain.run(input=input("Human: ")))


