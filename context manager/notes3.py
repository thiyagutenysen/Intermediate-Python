# way 2: using function with decorator
from contextlib import contextmanager


@contextmanager
def open_file(file_name, file_mode):
    f = open(file_name, file_mode)
    # everything before the yield statement is equivalent to __enter__ method in notes2.py
    yield f
    # everything after the yield statement is equivalent to __exit__ method in notes2.py
    f.close()


# the below line will run everything upto the yield statement
with open_file("sample4.txt", "w") as f:
    f.write("Is the file closed = " + str(f.closed))
# after we exit the with block, everything after the yield statement will run

print(f.closed)


# way 2 with safe implementation
@contextmanager
def open_file(file_name, file_mode):
    # this implementation ensures safety of tearing down resourse even when we run into errors
    # either try captures error or not, finally block will run
    try:
        f = open(file_name, file_mode)
        yield f
    finally:
        f.close()


with open_file("sample5.txt", "w") as f:
    f.write("Is the file closed = " + str(f.closed))

print(f.closed)
