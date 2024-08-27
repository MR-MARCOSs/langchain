from dotenv import load_dotenv
from langchain import hub
from langchain_openai import ChatOpenAI
from langchain_community.tools import YouTubeSearchTool
from langchain_community.tools.google_trends import GoogleTrendsQueryRun
from langchain_community.utilities.google_trends import GoogleTrendsAPIWrapper
from langchain.agents import create_openai_functions_agent, AgentExecutor
load_dotenv()

llm = ChatOpenAI(model='gpt-3.5-turbo', temperature=0)

youtube_tool = YouTubeSearchTool()
google_trends_tool = GoogleTrendsQueryRun(api_wrapper=GoogleTrendsAPIWrapper())
tools = [youtube_tool, google_trends_tool]
prompt = hub.pull('hwchase17/openai-functions-agent')
agent = create_openai_functions_agent(llm, tools, prompt)
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

agent_executor.invoke({'input':'Olá, tudo bem?'})

