print(" This line will always be run")  # this line will be executed irrespectively

if __name__ == "__main__":
    # the below line will only run when this file is directly executed
    # if this file executed from another file using any import methods, then the below line won't be executed
    print("This file high_level_use_case2's main method")
