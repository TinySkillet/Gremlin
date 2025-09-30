from dotenv import load_dotenv
from google import genai
from google.genai import types
import sys
import os

load_dotenv()

api_key = os.environ.get("GEMINI_API_KEY")


def main():
    args = sys.argv

    if len(args) < 2:
        print("Error! Prompt not provided!")
        sys.exit(1)

    user_prompt = args[1]

    if len(args) == 3 and args[-1] == "--verbose":
        verbose = True
    else:
        verbose = False

    client = genai.Client(api_key=api_key)

    messages = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)]),
    ]

    response = client.models.generate_content(
        model="gemini-2.0-flash-001",
        contents=messages,
    )

    print("Response: ", response.text)

    if verbose:
        metadata = response.usage_metadata
        print("Tokens used for prompt: ", metadata.prompt_token_count)
        print("Tokens used for response: ", metadata.candidates_token_count)


if __name__ == "__main__":
    main()
