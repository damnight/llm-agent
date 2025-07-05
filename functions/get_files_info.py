import os


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
