import os
import requests
from langchain import hub
from bs4 import BeautifulSoup
from langchain.agents import tool
from langchain_openai import ChatOpenAI
from langchain.agents import AgentExecutor
from langchain.agents import create_tool_calling_agent
from langchain_community.retrievers import WikipediaRetriever

os.environ['OPENAI_API_KEY'] = 'YOUR_OPENAI_API_KEY'
prompt = hub.pull("hwchase17/openai-functions-agent")

@tool
def get_location_weather(city_name: str) -> str:
    """Get the temperature in a given place"""
    url = f'https://www.google.com/search?q=weather+{city_name}'
    soup = BeautifulSoup(requests.get(url).content, features='html.parser')
    
    # Extract relevant information
    temperature = soup.find('div', attrs={'class': 'BNeawe iBp4i AP7Wnd'}).text
    conditions = soup.find('div', attrs={'class': 'BNeawe tAd8D AP7Wnd'}).text.split('\n')[-1]
    
    return f'Temperature: {temperature}\nConditions: {conditions}'

@tool
def get_wikipedia_information(query: str) -> str:
    """Get information about a topic from Wikipedia"""
    retriever = WikipediaRetriever()
    return retriever.invoke(query)[0].page_content

def call_agent(query: str) -> str:
    llm = ChatOpenAI() # Set up the agent's LLM
    tools = [get_location_weather, get_wikipedia_information] # Define the list of tools the agent can use
    agent = create_tool_calling_agent(llm, tools, prompt) # Create an agent that can call these tools
    agent_executor = AgentExecutor(agent=agent, tools=tools) # Create an AgentExecutor that can repeatedly call the agent and execute tools
    
    # And, finally, call the agent and return the output
    return agent_executor.invoke({'input': query})['output']