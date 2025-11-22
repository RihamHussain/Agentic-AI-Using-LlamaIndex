import os
import asyncio
from dotenv import load_dotenv
from tavily import AsyncTavilyClient
from llama_index.llms.google_genai import GoogleGenAI

load_dotenv()

tavily_api_key = os.environ["TAVILY_API_KEY"]
google_api_key = os.environ["GOOGLE_API_KEY"]

# Gemini model
llm = GoogleGenAI(
    model="gemini-2.0-flash",
    api_key=google_api_key
)

# --- Tavily Web Search Function (async) ---
async def search_web_async(query: str):
    client = AsyncTavilyClient(api_key=tavily_api_key)
    return await client.search(query=query)

# --- Wrapper to run async code safely ---
def search_web(query: str):
    return asyncio.run(search_web_async(query))


# --- Combined logic (ALL sync → required by LlamaIndex) ---
def ask_with_web_support(question: str):
    print("\n🔍 Searching the web...")

    # Step 1: real web search
    web_data = search_web(question)

    # Step 2: process through Gemini (sync)
    prompt = f"""
Use the following real web search results to answer this question accurately.

Question:
{question}

Search Results:
{web_data}

Provide an accurate final answer with citations.
"""

    response = llm.complete(prompt)
    return response.text


# --- Run the script ---
if __name__ == "__main__":
    question = "Latest news about Nvidia AI chips this week"
    answer = ask_with_web_support(question)
    print("\n🤖 Gemini Final Answer:\n")
    print(answer)
