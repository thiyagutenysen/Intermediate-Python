class open_file:
    def __init__(self, file_name, file_mode):
        self.file_name = file_name
        self.file_mode = file_mode

    def __enter__(self):
        self.file = open(self.file_name, self.file_mode)
        return self.file

    def __exit__(self, exc_type, exc_value, traceback):
        print("we are closing the file")
        self.file.close()


with open_file("sample8.txt", "w") as f:
    f.write("Is the file closed = " + str(f.closed))
    error

print(f.closed)

# Simple context manager class without "try and finally" itself is fully safe
# we do not need "try and except" in way1, which is using class
