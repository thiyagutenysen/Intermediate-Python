# context managers allow us to properly manage resources,
# so that we can specify exactly what we want to setup and tear down when working with certain objects

# Simple example with files:

# usual method 1
f = open("sample1.txt", "w")
f.write("chella writing code in notes1.py")
f.close()

# using context manager, method 2
with open("sample2.txt", "w") as f:
    f.write("chella writing code in notes1.py")
# we can say something as context manager if it uses "with" keyword
# if we use context manager, we do not need to remember to close down the file
# This method is highly recomended bcz,
# if the code throws an error inbetween working with the file then f.close() will not be executed and it will cause problem later,
# but if we use context manager, even if it throws inbetween working with the file, the file will be properly closed
# context manager handles the tear down of the resourses by itself, so that we don't have to worry

# Uses of context managers
# 1. databases
# 2. acquire and release locks
# 3. etc.,
