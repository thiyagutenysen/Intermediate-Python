# decorators with class
class decorator_class:
    # we use the the init method to get the argument original function
    def __init__(self, original_function):
        self.original_function = original_function

    # dunder __call__ function is the wrapper function here
    # we need to get *args and **kwargs inorder to decorate original functions with arguments
    def __call__(self, *args, **kwargs):
        print(
            "wrapper function executed this functionality, functionality is to present you the original function name, which is = ",
            self.original_function.__name__,
        )
        return self.original_function(*args, **kwargs)


@decorator_class
def display():
    print("display function ran")


@decorator_class
def display_info(name, age):
    print("Display info ran with arguments =", name, age)


display()
display_info("benjamin Engel", 21)
