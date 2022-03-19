import os
from contextlib import contextmanager

# ***************************************
# setup resources - save the current directory name to a variable and move to destination directory
# teardown resources - move back to the original directory from which we started
# ***************************************


@contextmanager
def change_dir(destination):
    try:
        cwd = os.getcwd()
        os.chdir(destination)
        yield
    finally:
        os.chdir(cwd)


with change_dir("dummy dir one"):
    print(os.listdir())

with change_dir("dummy dir two"):
    print(os.listdir())
