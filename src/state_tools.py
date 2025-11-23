import os
import sys
import asyncio
from dotenv import load_dotenv
from llama_index.llms.google_genai import GoogleGenAI
from llama_index.core.agent.workflow import AgentWorkflow
from llama_index.core.workflow import Context
from llama_index.core.workflow import JsonSerializer
import json

load_dotenv()

# 1. Setup Keys
tavily_api_key = os.environ.get("TAVILY_API_KEY")
google_api_key = os.environ.get("GOOGLE_API_KEY")

if not tavily_api_key or not google_api_key:
    # Just a warning to prevent crash if you only want to test the LLM part
    print("Warning: Keys missing. Ensure .env is set.")

# 2. Setup Gemini
llm = GoogleGenAI(
    model="gemini-2.0-flash", 
    api_key=google_api_key
)

# 3. Define Tools
async def set_name(ctx: Context, name: str) -> str:
    # Use ctx.store.get instead of ctx.get
    # We default to an empty dict or the initial state structure if not found
    state = await ctx.store.get("state", default={"name": "unset"})
    
    state["name"] = name
    
    # Use ctx.store.set instead of ctx.set
    await ctx.store.set("state", state)
    
    return f"Name set to {name}"

async def set_age(ctx: Context, age: int) -> str:
    # Use ctx.store.get instead of ctx.get
    # We default to an empty dict or the initial state structure if not found
    state = await ctx.store.get("state", default={"age": "unset"})
    
    state["age"] = age
    
    # Use ctx.store.set instead of ctx.set
    await ctx.store.set("state", state)
    
    return f"Age set to {age}"

# 4. Main Execution Function
async def main():
    workflow = AgentWorkflow.from_tools_or_functions(
        [set_name, set_age],
        llm=llm,
        system_prompt="You are an agent that must extract the user's name and age and use the set_name and set_age tools to store them.",
        initial_state={"name": "unset", "age": "unset"},
    )

    # Initialize Context with the workflow
    ctx = Context(workflow)

    # Run the workflow
    response = await workflow.run(
        user_msg="My name is Riham Hussain and I am 24 years old",
        ctx=ctx
    )
    print("Response:", str(response))

    # --- UPDATED SECTION ---
    # Use ctx.store.get to retrieve the state
    state = await ctx.store.get("state")
    
    print("Stored name:", state["name"])
    print("Stored age:", state["age"])

    # --- Saving State to File ---

    ctx_dict = ctx.to_dict(serializer=JsonSerializer())
    # save the dictionary to a file
    with open(".\\data\\statetools.json", "w") as f:
        json.dump(ctx_dict, f)

# 5. Run Script
if __name__ == "__main__":
    if sys.platform.startswith("win"):
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

    asyncio.run(main())