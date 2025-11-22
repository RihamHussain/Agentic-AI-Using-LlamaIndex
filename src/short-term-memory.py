import os
import sys
import asyncio
from dotenv import load_dotenv
from tavily import TavilyClient
from llama_index.llms.google_genai import GoogleGenAI
from llama_index.core.agent.workflow import AgentWorkflow

from llama_index.core.workflow import Context

load_dotenv()

# 1. Setup Keys
tavily_api_key = os.environ.get("TAVILY_API_KEY")
google_api_key = os.environ.get("GOOGLE_API_KEY")

if not tavily_api_key or not google_api_key:
    raise ValueError("Please set TAVILY_API_KEY and GOOGLE_API_KEY in your .env file")

# 2. Setup Gemini
llm = GoogleGenAI(
    model="gemini-2.0-flash",
    api_key=google_api_key
)

# 3. Define the Tool
def search_web(query: str) -> str:
    """
    Searches the web for the given query using Tavily.
    """
    print(f"   > searching for: {query}")
    client = TavilyClient(api_key=tavily_api_key)
    return str(client.search(query=query))

# 4. Main Execution Function
async def main():
    workflow = AgentWorkflow.from_tools_or_functions(
        [search_web],
        llm=llm,
        system_prompt="You are a helpful assistant. always check the web for current info."
    )

    # configure a context to work with our workflow
    ctx = Context(workflow)

    response = await workflow.run(
        user_msg="My name is Riham Hussain, nice to meet you!", ctx=ctx # give the configured context to the workflow
    )
    print("First Respose is:",str(response))

    # run the workflow again with the same context
    response = await workflow.run(user_msg="What is my name?", ctx=ctx)
    print("Second Response is:", str(response))

# 5. Run the Script (With Windows Fix)
if __name__ == "__main__":
    if sys.platform.startswith("win"):
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    # ----------------------------

    asyncio.run(main())