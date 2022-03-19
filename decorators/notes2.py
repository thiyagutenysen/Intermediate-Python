# original function with arguments


def decorator_function(original_function):
    def wrapper_function(*args, **kwargs):
        print(
            "wrapper function executed this functionality, functionality is to present you the original function name, which is = ",
            original_function.__name__,
        )
        return original_function(*args, **kwargs)

    return wrapper_function


@decorator_function
def display():
    print("display function ran")


@decorator_function
def display_info(name, age):
    print("Display info ran with arguments =", name, age)


display()
display_info("benjamin Engel", 21)
# here we wrapped two functions with the same wrapper
# we wrapped original functions with arguments too, using *args and **kwargs
