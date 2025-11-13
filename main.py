import os
import sys
import argparse
from dotenv import load_dotenv
from google import genai
from google.genai import types


def main():
    load_dotenv()
    api_key = os.environ.get('GEMINI_API_KEY')
    client = genai.Client(api_key = api_key)

    # Get prompt from command line
    # try:
    #     text_prompt = sys.argv[1]
    #     print(type(text_prompt))
    # except:
    #     print('ERROR: No prompt found')
    #     sys.exit(1)
    
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

    response = client.models.generate_content(
        model = 'gemini-2.0-flash-001',
        contents = messages
    )

    print(response.text)

    if args.verbose:
        print(f"User prompt: {args.text_prompt}")
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")

if __name__ == "__main__":
    main()
