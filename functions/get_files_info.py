import os

from functions.file_utils import check_path


def get_files_info(working_directory, directory=None):
    try:
        target_abs_path, is_in_workdir, is_dir = check_path(
            working_directory, directory
        )
        if not is_in_workdir:
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
        if not is_dir:
            return f'Error: "{directory}" is not a directory'

        listdir_str = ""
        for file in os.listdir(target_abs_path):
            current_file_path = os.path.join(target_abs_path, file)
            current_file_size = os.path.getsize(current_file_path)
            listdir_str += f"- {file}: file_size={current_file_size} bytes, is_dir={os.path.isdir(current_file_path)}\n"
        return listdir_str
    except Exception as e:
        return f"Error: {e}"
