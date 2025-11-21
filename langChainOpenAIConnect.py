# This program demonstrates a simple integration of LangChain with OpenAI's Chat API. It uses a prompt template to summarize a given piece of information.


from dotenv import load_dotenv 
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI

load_dotenv()
import os 
if not os.getenv("OPENAI_API_KEY"):
    raise RuntimeError("OPENAI_API_KEY not set. Add it to .env or export in your shell.")


def main():
    print("Hello from langchain!")
    information = """World War II was a global war that lasted from 1939 to 1945, involving most of the world's nations. It was the most widespread war in history, with more than 100 million people serving in military units. The war began with the invasion of"""
    summary_template = """
    Summarize the following information in a concise manner:
    {information}"""
    
    summary_prompt_template = PromptTemplate(
        input_variables= ["information"], template=summary_template
    )
    llm = ChatOpenAI(temperature=0, model="gpt-5")
    chain = summary_prompt_template | llm
    
    response = chain.invoke(input={"information": information})
    print(response.content)
    
    
if __name__ == "__main__":
    main()
 