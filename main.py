import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types



load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)



def main():

    print("Hello from llm-agent!")
    
    args = sys.argv
    if len(args) < 2:
        print("No prompt was given")
        sys.exit(1)
    verbose = False
    if "--verbose" in args:
        verbose = True

    question = args[1]
    messages = [types.Content(role="user", parts=[types.Part(text=question)])]
    response = client.models.generate_content(
        model='gemini-2.0-flash-001', contents=messages
        )
    if verbose:
        print(f"User prompt: {question}")   
        usage = f"Prompt tokens: {response.usage_metadata.prompt_token_count}" \
            f"\nResponse tokens: {response.usage_metadata.candidates_token_count}"
        print(usage)

    print(response.text)




if __name__ == "__main__":
    main()
