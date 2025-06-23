import os

from functions.file_utils import get_file_data


def get_files_info(working_directory, directory=None):
    try:
        file_data = get_file_data(working_directory, directory)
        path = file_data["path"]
        is_dir = file_data["is_dir"]
        is_in_workdir = file_data["is_in_workdir"]

        if not is_in_workdir:
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
        if not is_dir:
            return f'Error: "{directory}" is not a directory'

        result = []
        for file in os.listdir(path):
            current_file_path = os.path.join(path, file)
            current_file_size = os.path.getsize(current_file_path)
            result.append(f"- {file}: file_size={current_file_size} bytes, is_dir={os.path.isdir(current_file_path)}")

        return "\n".join(result)

    except Exception as e:
        return f"Error: {e}"
