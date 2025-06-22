import os

from functions.file_utils import get_file_data


MAX_CHARS = 10000


def get_file_content(working_directory, file_path):
    try:
        file_data = get_file_data(working_directory, file_path)
        path = file_data["path"]
        is_file = file_data["is_file"]
        is_in_workdir = file_data["is_in_workdir"]

        if not is_in_workdir:
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
        if not is_file:
            return f'Error: File not found or is not a regular file: "{file_path}"'

        with open(path, "r") as f:
            file_content = f.read(MAX_CHARS)

    except Exception as e:
        print(f"Error: {e}")
