if __name__ == "__main__":
    print("run directly")
else:
    print("run from import")

# if we create a new python file randomly named index.py and import this file
# "import high_level_usecase"
# output will be "run from import", which is the else statements
# instead of running index.py, if we run this file directly, we will get the output: "run directly"
