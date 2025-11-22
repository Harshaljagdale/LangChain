#Search agent using Tavily tool

from dotenv import load_dotenv

load_dotenv()

import os
from langchain.agents import create_agent
from langchain.tools import tool
from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from langchain_tavily import TavilySearch


llm = ChatOpenAI(temperature=0, verbose=True)
tools = [TavilySearch]
agent = create_agent(model=llm,tools=tools)

def main():
    print ("Welcome to the TAVILIY Demo!")
    result = agent.invoke({"messages":HumanMessage(content="What is the weather in Tokyo today?")})    
    print(result)
    
if __name__ == "__main__":
    main()