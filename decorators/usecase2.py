import time


def my_timer(original_function):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = original_function(*args, **kwargs)
        end = time.time()
        print("[{}] ran in: {} sec".format(original_function.__name__, end - start))
        return result

    return wrapper


@my_timer
def display_info2(name, age):
    print("display_info ran with arguments ({}, {})".format(name, age))


display_info2("Tom", 22)

# usecase
# instead of writing code to calculate function execution time in each function,
# we can write a generic and common function that can calculate execution time for all the functions,
# by just using a wrapper
