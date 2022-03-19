from contextlib import contextmanager


@contextmanager
def open_file(file_name, file_mode):
    f = open(file_name, file_mode)
    yield f
    print("we are closing the file")
    f.close()


with open_file("sample6.txt", "w") as f:
    f.write("Is the file closed = " + str(f.closed))
    error

print(f.closed)


# Simple context manager function without "try and finally" is not at all safe
