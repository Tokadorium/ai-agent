import os


def get_file_data(working_directory, target):
    try:
        target = target or ""
        workdir_abs_path = os.path.abspath(working_directory)
        target_abs_path = os.path.abspath(os.path.join(working_directory, target))
        file_data = {
            "parent_dir": os.path.dirname(target_abs_path),
            "path": target_abs_path,
            "is_dir": os.path.isdir(target_abs_path),
            "is_file": os.path.isfile(target_abs_path),
            # "is_in_workdir": target_abs_path.startswith(os.path.abspath(working_directory))
            "is_in_workdir": os.path.commonpath([target_abs_path, workdir_abs_path]) == workdir_abs_path
        }
    except Exception as e:
        raise e

    return file_data
