# We first need to understand first-class functions and closures inorder to study decorators
# Decorators - Dynamically alter the functionality of your function

# Decorator is a function that takes another function as argument as some kind of functionality and then,
# returns another function, all of this without altering the source code of the original function that you passes in


def decorator_function(original_function):
    def wrapper_function():
        return original_function()

    return wrapper_function


def display():
    print("display function ran")


decorated_display = decorator_function(display)
decorated_display()
print("******************************************************")

# why do we wanna do the above shit
# decorating our function allows us to easily add functionality to our existing functions,
# by adding that functionality inside a wrapper
def decorator_function(original_function):
    def wrapper_function():
        # extra functionality is in the below block
        ##############################
        print(
            "wrapper function executed this functionality, functionality is to present you the original function name, which is = ",
            original_function.__name__,
        )
        ###############################
        return original_function()

    return wrapper_function


def display():
    print("display function ran")


decorated_display = decorator_function(display)
decorated_display()
print("******************************************************")

# Another method and beautiful way to do the above same things
def decorator_function(original_function):
    def wrapper_function():
        # extra functionality is in the below line
        print(
            "wrapper function executed this functionality, functionality is to present you the original function name, which is = ",
            original_function.__name__,
        )
        return original_function()

    return wrapper_function


@decorator_function  # -----> this line is same as "display = decorator_function(display)"
def display():
    print("display function ran")


# decorated_display = decorator_function(display)
display()

# the problem with the above methods is that it only works when the original function that doesn't require any arguments
# the solution is to add *args and **kwargs in the wrapper function,
# we also need to pass these into the original function
# let's see this in the next note
