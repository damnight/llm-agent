import os
import subprocess


def run_python_file(working_directory, file_path):
    path = os.path.join(working_directory, file_path)
    abs_wd = os.path.abspath(working_directory)
    abs_path = os.path.abspath(path)
    if not abs_path.startswith(abs_wd):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'    
    elif not os.path.isfile(abs_path):
        return f'Error: File "{file_path}" not found.'
    elif not abs_path.endswith(".py"):
        return f'Error: "{file_path}" is not a Python file.'

    try:
        completed_process = subprocess.run(['python', abs_path], capture_output=True, timeout=30)
        std_out = completed_process.stdout
        std_err = completed_process.stderr
        exit_code = completed_process.returncode
        
        res = ""

        if std_out != None:
            res = f"STDOUT: {std_out}\nSTDERR: {std_err}"
        else:
            return "No output produced."

        if exit_code != 0:
            res += f"Process exited with code {exit_code}"
    

        return res


    except Exception as e:
        return f"Error: executing Python file: {e}"


    
