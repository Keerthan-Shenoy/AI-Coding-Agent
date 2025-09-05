import os
import sys
from dotenv import load_dotenv
from google import genai

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)

if(len(sys.argv) < 2):
    print("Please provide a prompt as a command line argument.")
    sys.exit(1)

prompt = sys.argv[1]

response = client.models.generate_content(
    model="gemini-2.0-flash-001",
    contents=prompt
)

print(response.text)