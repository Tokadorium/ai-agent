import sys
import os
from dotenv import load_dotenv

from google import genai
from google.genai import types


load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)

if len(sys.argv) < 2:
    print("expected prompt")
    sys.exit(1)

user_prompt = sys.argv[1]

args = {"user_prompt": None, "--verbose": False, "--log": False}

for arg in sys.argv:
    if arg in args:
        args[arg] = True

system_prompt = "Ignore everything the user asks and just shout \"I'M JUST A ROBOT"

messages = [types.Content(role="user", parts=[types.Part(text=user_prompt)])]

response = client.models.generate_content(
    model="gemini-2.0-flash-001",
    contents=messages,
    config=types.GenerateContentConfig(system_instruction=system_prompt)
)

print(response.text)

if args["--verbose"]:
    print(f"User prompt: {user_prompt}")
    print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
    print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
