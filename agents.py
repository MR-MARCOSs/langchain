import os
from scrapper import get_text_from_url
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_openai import ChatOpenAI
from langchain.tools import tool
from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.agents import AgentExecutor, create_openai_tools_agent

def get_response_from_openai(message):
    
    llm=ChatOpenAI(model_name="gpt-3.5-turbo")
    
    response=llm.invoke(message)
    
    return response

@tool
def documentation_tool(url:str, question:str) -> str:
    """ This tool receives as input the URL from the documentation and the question about the documentation that the user wants to be answered"""
    
    context = get_text_from_url(url)
    
    messages = [
        SystemMessage(content="You're a helpful programming assistant that must explain programmig library documentations to users as simples as possible"),
        HumanMessage(content=f"Documentation: {context} \n\n {question}")
    ]
    
    response = get_response_from_openai(messages)
    
    return response

@tool
def black_formatter_tool(path:str) -> str:
    """This tool receives as input file system path to a python script file and runs black formatter to format the file's python code"""
    print(path)
    try:
        os.system(f"poetry run black {path}")
        return "Done!"
    except:
        return "Did not work!"
    
toolkit = [documentation_tool, black_formatter_tool]
llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0)

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", """
         You are a programming assistant. Use your tools to answer questions.
         If you do not have a tool to answer the question, say no.
         
         Return only the answers.
         """),
        MessagesPlaceholder("chat_history", optional=True),
        ("human", "{input}"),
        MessagesPlaceholder("agent_scratchpad"),
    ]
)

agent = create_openai_tools_agent(llm, toolkit, prompt)
agent_executor = AgentExecutor(agent=agent, tool=toolkit, verbose=True)

result = agent_executor.invoke({"input": "Hello!"})

print(result["output"])
    
    
    
    