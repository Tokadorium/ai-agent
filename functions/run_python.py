import subprocess

from functions.file_utils import get_file_data


def run_python_file(working_directory, file_path):
    try:
        file_data = get_file_data(working_directory, file_path)
    except Exception as e:
        print(f"Error: {e}")

    path = file_data["path"]
    parent_dir = file_data["parent_dir"]
    is_file = file_data["is_file"]
    is_in_workdir = file_data["is_in_workdir"]

    if not is_in_workdir:
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    if not is_file:
        return f'Error: File "{file_path}" not found.'
    if not path.endswith(".py"):
        return f'Error: "{file_path}" is not a Python file.'

    try:
        process = subprocess.run(["python", path], cwd=parent_dir, timeout=30, capture_output=True)
    except Exception as e:
        return f"Error: executing Python file: {e}"

    output = ""

    output += f"STDOUT: {process.stdout if process.stdout != None else "No output produced"}\n"
    output += f"STDERR: {process.stderr}\n"
    if process.returncode != 0:
        output += f"Process exited with code {process.returncode}\n"

    return output