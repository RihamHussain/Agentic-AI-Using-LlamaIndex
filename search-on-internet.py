import os
import sys
import asyncio
from dotenv import load_dotenv
from tavily import TavilyClient
from llama_index.llms.google_genai import GoogleGenAI
from llama_index.core.agent.workflow import AgentWorkflow

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

    print("🤖 Agent is thinking...")
    
    response = await workflow.run(user_msg="What is the current weather in San Francisco?")
    
    print("\nFINAL ANSWER:")
    print(str(response))
    
    # Small pause to let connections close gracefully (optional but helpful)
    await asyncio.sleep(0.1)

# 5. Run the Script (With Windows Fix)
if __name__ == "__main__":
    # --- WINDOWS SPECIFIC FIX ---
    # This prevents the "Fatal error on SSL transport" crash on Windows
    if sys.platform.startswith("win"):
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    # ----------------------------

    asyncio.run(main())