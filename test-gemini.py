import os
from dotenv import load_dotenv
from llama_index.llms.google_genai import GoogleGenAI

load_dotenv()

# FIX: Use a model that actually exists in your list. 
# We are using 'gemini-2.0-flash' based on your check_models.py output.
llm = GoogleGenAI(
    model="gemini-2.0-flash", 
    api_key=os.environ["GOOGLE_API_KEY"]
)

try:
    response = llm.complete("Hello! Who are you and what version of Gemini are you?")
    print("Response:\n", response.text)
except Exception as e:
    print(f"Error: {e}")