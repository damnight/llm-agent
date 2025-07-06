from google.genai import types
from functions.get_files_info import get_file_content, get_files_info, write_file
from functions.run_python import run_python_file



def call_function(function_call_part, verbose=False):
    if verbose:
       print(f"Calling function: {function_call_part.name}({function_call_part.args})")
    else:
        print(f" - Calling function: {function_call_part.name}")

    fnc_lexicon = {
        "write_file": write_file,
        "get_file_content": get_file_content,
        "get_files_info": get_files_info,
        "run_python_file": run_python_file,
    }

    wd = "./calculator"
    args = function_call_part.args.copy()
    args["working_directory"] = wd

    fnc_name = function_call_part.name

    try:
        fnc =  fnc_lexicon[fnc_name]
        fnc_res = fnc(**args)
        return types.Content(
           role="tool",
           parts=[
               types.Part.from_function_response(
                   name=fnc_name,
                   response={"result": fnc_res},
               )
           ],
        )
        
    except Exception as e:
        return types.Content(
           role="tool",
           parts=[
               types.Part.from_function_response(
                   name=fnc_name,
                   response={"error": f"Unknown function: {fnc_name}"},
               )
          ],
        )
