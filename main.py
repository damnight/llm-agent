import os
import sys
from dotenv import load_dotenv
from google import genai
from functions.call_function import call_function
from google.genai import types
from functions.get_files_info import schema_get_files_info, schema_get_file_content, schema_write_file
from functions.run_python import schema_run_python_file



load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)



def main():

    print("Hello from llm-agent!")
    
    system_prompt = ""
    available_functions = types.Tool(
        function_declarations=[
            schema_get_files_info,
            schema_get_file_content,
            schema_write_file,
            schema_run_python_file,
        ]
    )

    try:
        with open(".system_prompt") as f:
           system_prompt = f.read()

    except FileNotFoundError as e:
        print(f"Error: file not found, verify file integrity and retry")
        sys.exit(1)
    except Exception as e:
        print(f"Error: unknown error: {e}")
        sys.exit(1)
    args = sys.argv
    if len(args) < 2:
       print("No prompt was given")
       sys.exit(1)
          
    verbose = False
    if "--verbose" in args:
        verbose = True
    
    question = args[1]
    messages = [types.Content(role="user", parts=[types.Part(text=question)])]  


    max_reps = 20
    reps = 0
    while reps < max_reps:

        response = client.models.generate_content(
              model='gemini-2.0-flash-001', 
              contents=messages,
              config=types.GenerateContentConfig(tools=[available_functions], system_instruction=system_prompt)
        )
          
        if response.function_calls != None:
            for can in response.candidates:
                messages.append(can.content)

            for call in response.function_calls:
                print(f"Calling function:{call.name}({call.args}\n")
                try:
                    res = call_function(call, verbose)
                    messages.append(res)
                    if verbose:
                        print(f"-> {res.parts[0].function_response.response}")
                        reps += 1
                except Exception as e:
                   raise e
        else:
            if verbose:
                print(f"User prompt: {question}")   
                usage = f"Prompt tokens: {response.usage_metadata.prompt_token_count}" \
                    f"\nResponse tokens: {response.usage_metadata.candidates_token_count}"
                print(usage)
            
            print(response.text)
            break

if __name__ == "__main__":
    main()
