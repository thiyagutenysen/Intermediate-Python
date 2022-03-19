import logging
import time


def my_timer(original_function):
    def wrapper1(*args, **kwargs):
        start = time.time()
        result = original_function(*args, **kwargs)
        end = time.time()
        print("[{}] ran in: {} sec".format(original_function.__name__, end - start))
        return result

    return wrapper1


def my_logger(original_function):
    logging.basicConfig(
        filename="{}.log".format("functions_executed"), level=logging.INFO
    )

    def wrapper2(*args, **kwargs):
        logging.info(
            "[{}] Ran with args: {}, and kwargs: {}".format(
                original_function.__name__, args, kwargs
            )
        )
        return original_function(*args, **kwargs)

    return wrapper2


@my_timer  ### -----> this and the below line is same as: display_info4 = my_timer(my_logger(display_info4)),
@my_logger  ### by understanding the above comment code's function flow, we can understand this code
def display_info3(name, age):
    print("display_info ran with arguments ({}, {})".format(name, age))


display_info3("Tom", 22)
# This calculates function execution time along with log statement execution
# this logs "display_info3" as function name

# decorators are executed bottom to top

print(display_info3.__name__)
