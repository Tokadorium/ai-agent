from functions.file_utils import get_file_data


def run_python_file(working_directory, file_path):
    try:
        file_data = get_file_data(working_directory, file_path)
        path = file_data["path"]
        is_file = file_data["is_file"]
        is_in_workdir = file_data["is_in_workdir"]

        if not is_in_workdir:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
        if not is_file:
            return f'Error: File "{file_path}" not found.'
        if not path.endswith(".py"):
            return f'Error: "{file_path}" is not a Python file.'

    except Exception as e:
        print(f"Error: {e}")
