import os
from google import genai
from google.genai import types
from dotenv import load_dotenv
from sys import argv, exit

load_dotenv()
API_KEY = os.environ.get("GEMINI_API_KEY")


def main():

    if not API_KEY:
        print("GEMINI_API_KEY not found in .env!")
        exit(1)

    args = len(argv)

    if args < 2:
        print("Prompt required!")
        exit(1)

    if argv[-1] == "--verbose":
        verbose = True
    else:
        verbose = False

    user_prompt = argv[1]

    messages = [types.Content(role="user", parts=[types.Part(text=user_prompt)])]

    client = genai.Client(api_key=API_KEY)
    response = client.models.generate_content(
        model="gemini-2.0-flash-001",
        contents=messages,  
    )

    print(response.text)

    if verbose:
        print("Tokens in prompt: ", response.usage_metadata.prompt_token_count)
        print("Tokens in response: ", response.usage_metadata.candidates_token_count)


if __name__ == "__main__":
    main()
