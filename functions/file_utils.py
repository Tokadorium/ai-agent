import os


def check_path(working_directory, target):
    try:
        target_abs_path = os.path.abspath(os.path.join(working_directory, target))
        file_data = {
            "path": target_abs_path,
            "is_dir": os.path.isdir(target_abs_path),
            "is_file": os.path.isfile(target_abs_path),
            "is_in_workdir": target_abs_path.startswith(os.path.abspath(working_directory))
        }
    except Exception as e:
        raise e

    return file_data
