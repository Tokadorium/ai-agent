import sys

from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content
from functions.write_file import write_file
from functions.run_python import run_python_file


test_cases = {
    "get_files_info": {
        "func": get_files_info,
        "args": [
            ("calculator", "."),
            ("calculator", "pkg"),
            ("calculator",),
            ("calculator", "/bin"),
            ("calculator", "../")
        ]
    },
    "get_file_content": {
        "func": get_file_content,
        "args": [
            ("calculator", "lorem.txt"),
            ("calculator", "main.py"),
            ("calculator", "pkg/calculator.py"),
            ("calculator", "/bin/cat")
        ]
    },
    "write_file": {
        "func": write_file,
        "args": [
            ("calculator", "lorem.txt", "wait, this isn't lorem ipsum"),
            ("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet"),
            ("calculator", "/tmp/temp.txt", "this should not be allowed")
        ]
    },
    "run_python_file": {
        "func": run_python_file,
        "args": [
            ("calculator", "main.py"),
            ("calculator", "tests.py"),
            ("calculator", "../main.py"),
            ("calculator", "nonexistent.py")
        ]
    }
}

test_group = test_cases.get(sys.argv[1])

if test_group:
    func = test_group["func"]
    for args in test_group["args"]:
        print(func(*args))