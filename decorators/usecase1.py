import logging


def my_logger(original_function):
    logging.basicConfig(
        filename="{}.log".format("functions_executed"), level=logging.INFO
    )

    def wrapper(*args, **kwargs):
        logging.info(
            "[{}] Ran with args: {}, and kwargs: {}".format(
                original_function.__name__, args, kwargs
            )
        )
        return original_function(*args, **kwargs)

    return wrapper


@my_logger
def display_info1(name, age):
    print("display_info ran with arguments ({}, {})".format(name, age))


# @my_logger is equal to "display_info1 = my_logger(display_info1)
# my_logger function is already called when we declare @my_logger
# therefore display_info1 is equal to wrapper
# In the below line we are just calling the wrapper function
display_info1("Tom", 22)

# The usecase is
# instead of writing log statements in each function,
# we can write a single common logger function and use it to wrap all the functions
# As a result we will write less code
