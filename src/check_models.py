import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

api_key = os.environ.get("GOOGLE_API_KEY")

if not api_key:
    print("Error: GOOGLE_API_KEY not found in environment.")
else:
    print(f"Key found: {api_key[:5]}...{api_key[-3:]}")
    
    try:
        client = genai.Client(api_key=api_key)
        print("\n--- Attempting to list models ---")
        # We iterate specifically looking for 'generateContent' capable models
        for m in client.models.list():
            if "gemini" in m.name:
                print(f"Found: {m.name}")
                
    except Exception as e:
        print(f"\nCRITICAL ERROR: {e}")
        print("\nPossible fixes:")
        print("1. Go to https://aistudio.google.com/app/apikey and ensure the key is Active.")
        print("2. Make sure you selected 'Create API Key in new project' (simplest option).")