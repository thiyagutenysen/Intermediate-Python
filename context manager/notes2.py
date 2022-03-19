# We will create our own context manager
# way1: class                               -----> this is automatically safe, works if our code has errors too
# way2: function with decorator             -----> this is safe only if we use "try and except"

# way 1: using classes
class open_file:
    def __init__(self, file_name, file_mode):
        self.file_name = file_name
        self.file_mode = file_mode

    # setup method for resources
    def __enter__(self):
        self.file = open(self.file_name, self.file_mode)
        return self.file

    # teardown method for resources
    def __exit__(self, exc_type, exc_value, traceback):
        self.file.close()


# open_file("sample3.txt", "w") - initializes the arguments sent into it
# with keyword then calls the __enter__ method and assingns the __enter__ return to f
with open_file("sample3.txt", "w") as f:
    f.write("Is the file closed = " + str(f.closed))
# when the program exits and come out of the with block, __exit__ method is automatically called

# Let's check whether the file is closed or not
print(f.closed)
# we can use the object or variable "f" out of it's scope(within the "with" block)
