import os

def get_files_info(working_directory, directory=None):
    try:
        target_path = os.path.join(working_directory, directory)
        target_path_abs = os.path.abspath(target_path)

        if not os.path.isdir(target_path_abs):
            return f'Error: "{directory}" is not a directory'
        if not target_path_abs.startswith(os.path.abspath(working_directory)):
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

        listdir_str = ""
        for file in os.listdir(target_path_abs):
            current_file_path = os.path.join(target_path_abs, file)
            current_file_size = os.path.getsize(current_file_path)
            listdir_str += f'- {file}: file_size={current_file_size} bytes, is_dir={os.path.isdir(current_file_path)}\n'
        return listdir_str
    except Exception as e:
        return f'Error: {e}'