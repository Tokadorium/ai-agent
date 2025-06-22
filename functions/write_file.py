import os

from functions.file_utils import get_file_data


def write_file(working_directory, file_path, content):
    try:
        file_data = get_file_data(working_directory, file_path)
        path = file_data["path"]
        parent_dir = file_data["parent_dir"]
        is_in_workdir = file_data["is_in_workdir"]

        if not is_in_workdir:
            return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'

        if not os.path.exists(parent_dir):
            os.makedirs(parent_dir)

        with open(path, "w") as f:
            f.write(content)

        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'

    except Exception as e:
        print(f"Error: {e}")
