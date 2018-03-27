import sys
import os


def append_if_not_exist(*path: str) -> list:
    for p in path:
        if p not in sys.path:
            sys.path.append(p)
    return sys.path


append_if_not_exist('/usr/local/lib/python3.5/dist-packages')
MY_PYTHON_PROJECT = os.getenv('MY_PYTHON_PROJECT')
append_if_not_exist(MY_PYTHON_PROJECT)
append_if_not_exist(f'{MY_PYTHON_PROJECT}/crawler')
append_if_not_exist(f'{MY_PYTHON_PROJECT}/crawler/finance')