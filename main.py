import os
import sys
import argparse
from dotenv import load_dotenv
from prompt import system_prompt
from google import genai
from google.genai import types
from config import MAX_ITERATIONS
from functions import *
from call_function import *

def main():
    load_dotenv()
    api_key = os.environ.get('GEMINI_API_KEY')
    client = genai.Client(api_key = api_key)
    
    # Handle argument parsing
    parser = argparse.ArgumentParser()
    parser.add_argument('text_prompt', type=str, help='The prompt used for the AI')
    parser.add_argument('--verbose', action='store_true', help='Enable verbose output')
    args = parser.parse_args()

    if not args.text_prompt:
        print('ERROR: No prompt found')
        sys.exit(1)

    messages = [
        types.Content(role="user", parts=[types.Part(text=args.text_prompt)])
    ]

    iteration_count = 0
    response = None
    while(response is None):
        iteration_count += 1
        if(iteration_count > MAX_ITERATIONS):
            print(f"Iterations have exceeded the maximum of {MAX_ITERATIONS}")
            sys.exit(1)
        try:
            response = generate_content(client, messages, args)
        except Exception as e:
            print(f"Error: {e}")
    print(response)

def generate_content(client, messages, args):
    response = client.models.generate_content(
        model = 'gemini-2.0-flash-001',
        contents = messages,
        config=types.GenerateContentConfig(
            tools=[available_functions], system_instruction=system_prompt
        ),
    )

    for candidate in response.candidates:
        messages.append(candidate.content)

    if args.verbose:
        print(f"User prompt: {args.text_prompt}")
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
    
    if not response.function_calls:
        return response.text

    call_result_history = []
    for function_call_part in response.function_calls:
        function_call_result = call_function(function_call_part, args.verbose)
        if not function_call_result.parts[0].function_response.response:
            raise Exception("ERROR: no function call result")
        call_result_history.append(function_call_result.parts[0])
        if args.verbose:
            print(f"-> {function_call_result.parts[0].function_response.response}")
    
    messages.append(types.Content(role="user", parts=call_result_history))


if __name__ == "__main__":
    main()
