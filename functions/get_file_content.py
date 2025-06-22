import os

from functions.file_utils import check_path

def get_file_content(working_directory, file_path):
    try:
        file_data = check_path(working_directory, directory)
        target_abs_path = file_data["path"]
        is_file = file_data["is_file"]
        is_in_workdir = file_data["is_in_workdir"]

        if not is_in_workdir:
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
        if not is_file:
            return f'Error: File not found or is not a regular file: "{file_path}"'
