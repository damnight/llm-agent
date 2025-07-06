import os

from google.genai import types


MAX_CHARS = 10000




def get_files_info(working_directory, directory=""):
    path = os.path.join(working_directory, directory)
    abs_wd = os.path.abspath(working_directory)
    abs_path = os.path.abspath(path)
    if not abs_path.startswith(abs_wd):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    elif not os.path.isdir(abs_path):
        return f'Error: "{directory}" is not a directory'
    
    result = ""
    dir_list = os.listdir(abs_path)

    for file in dir_list:
        file_size = os.path.getsize(os.path.join(abs_path, file))
        is_dir = os.path.isdir(os.path.join(abs_path, file))
        result += f"- {file}: file_size={file_size} bytes, is_dir={is_dir}\n"
    return result


def get_file_content(working_directory, file_path):
    path = os.path.join(working_directory, file_path)
    abs_wd = os.path.abspath(working_directory)
    abs_path = os.path.abspath(path)
    if not abs_path.startswith(abs_wd):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    elif not os.path.isfile(abs_path):
        return f'Error: File not found or is not a regular file: "{file_path}"'
    
    try:
        with open(abs_path, "r") as f:
            file_content_string = f.read(MAX_CHARS)
        
            if len(file_content_string) >= 10000:
                file_content_string += f"[...File \"{file_path}\" truncated at 10000 characters]"
        
            return file_content_string
    except FileNotFoundError as e:
        print(f"Error: FileNotFoundError: {e}")
    except IOError as e:
        print(f"Error: IOError: {e}")
    except Exception as e:
        print(f"Error: unkown error: {e}")

def write_file(working_directory, file_path, content):
    path = os.path.join(working_directory, file_path)
    abs_wd = os.path.abspath(working_directory)
    abs_path = os.path.abspath(path)
    if not abs_path.startswith(abs_wd):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    
    try:
        with open(abs_path, "w") as f:
            f.write(content)
            return f"Successfully wrote to file \"{abs_path}\" ({len(content)} characters written)"

    except FileNotFoundError as e:
        print(f"Error: FileNotFoundError: {e}")
    except IOError as e:
        print(f"Error: IOError: {e}")
    except Exception as e:
        print(f"Error: unkown error: {e}")



schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
            ),
        },
    ),
)

schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description="Prints entire file content as text, up to 10000 characters. If file exceeds character limit, the resulting text will reflect that at the end.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The relative path from your location to the file you want to execute",
            ),
        },
    ),
)
schema_write_file = types.FunctionDeclaration(
    name="write_file",
        description="Write file to path, create new if doesn't exist",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The relative path from your location to the file you want to write",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="The content which you want to write to the file. It will overwrite current",
            ),
        },
    ),
)

