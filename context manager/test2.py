from contextlib import contextmanager


@contextmanager
def open_file(file_name, file_mode):
    try:
        f = open(file_name, file_mode)
        yield f
    finally:
        print("we are closing the file")
        f.close()


with open_file("sample7.txt", "w") as f:
    f.write("Is the file closed = " + str(f.closed))
    error

print(f.closed)

# Simple context manager function with "try and finally" is fully safe
