from dotenv import load_dotenv
from langchain import hub
from langchain_openai import ChatOpenAI
from langchain_community.tools import YouTubeSearchTool
from langchain_community.tools.google_trends import GoogleTrendsQueryRun
from langchain_community.utilities.google_trends import GoogleTrendsAPIWrapper
from langchain.agents import create_openai_functions_agent, AgentExecutor, Tool
load_dotenv()

llm = ChatOpenAI(model='gpt-3.5-turbo', temperature=1)

youtube_tool = YouTubeSearchTool()

gtool= Tool(
    name="google_trends",
    description="Return information of google trends topics in the last year only, the input must be related to the user's query",
    func=GoogleTrendsQueryRun(api_wrapper=GoogleTrendsAPIWrapper())
)
tools = [youtube_tool, gtool]
prompt = hub.pull('hwchase17/openai-functions-agent')
agent = create_openai_functions_agent(llm, tools, prompt)
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

#agent_executor.invoke({'input':'Olá, tudo bem?'})
#agent_executor.invoke({'input':'Me recomende vídeos de propagandas de produtos de limpeza'})
agent_executor.invoke({'input':'qual tópico mais pesquisado e relevante agora?'})


