import sys
import os
from dotenv import load_dotenv

from google import genai
from google.genai import types

from config.function_declaration_types import available_functions
from config.system_prompt import system_prompt
from functions.call_function import call_function


load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

if len(sys.argv) < 2:
    print("expected prompt")
    sys.exit(1)

args = {"user_prompt": sys.argv[1], "--verbose": False, "--log": False}

for arg in sys.argv:
    if arg in args:
        args[arg] = True

messages = [
    types.Content(role="user", parts=[types.Part(text=args["user_prompt"])]),
]

for i in range(0, 20):
    response = client.models.generate_content(
        model="gemini-2.0-flash-001",
        contents=messages,
        config=types.GenerateContentConfig(
            system_instruction=system_prompt, tools=[available_functions]
        ),
    )

    for candidate in response.candidates:
        messages.append(candidate.content)

    function_calls_list = response.function_calls

    if function_calls_list:
        function_call_result = call_function(function_calls_list[0], args["--verbose"])

        if not function_call_result.parts[0].function_response.response:
            raise Exception("Fatal error: invalid response")

        if args["--verbose"]:
            print(f"-> {function_call_result.parts[0].function_response.response}")

        messages.append(function_call_result)
    else:
        print(response.text)
        if args["--verbose"]:
            print(f"User prompt: {args["user_prompt"]}")
            print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
            print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
        break
