# stacking decorators 1 and 2 have there limitations
# stacking decorator 1 code logs the function name correctly but calculates function time along with logging time
# stacking decorator 2  code calculates the function execution time correctly but logs the function name as wrapper,
#  and not it's original name

# So how do we fix this
# our aim is to get the original function execution time alone and preserve it's actual name too
# we are gonna use a decorator inside of a decorator
from functools import wraps  # -----> new code

import logging
import time


def my_timer(original_function):
    @wraps(original_function)  # -----> new code
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

    @wraps(original_function)  # -----> new code
    def wrapper2(*args, **kwargs):
        logging.info(
            "[{}] Ran with args: {}, and kwargs: {}".format(
                original_function.__name__, args, kwargs
            )
        )
        return original_function(*args, **kwargs)

    return wrapper2


@my_timer
@my_logger  # now, the order of stacking of decorators is irrelevant
def display_info5(name, age):
    print("display_info ran with arguments ({}, {})".format(name, age))


display_info5("Tom", 22)
print(display_info5.__name__)
# In this example, we do not need to keep track of which how the original function is inserted into multiple wrappers,
# and the we also don't need to care about the hierarchy of wrappers
# every wrapper uses the original (actual) function as it is, due to @wraps()


# Decorators are used a lot for class properties, routing for web framework, etc.,

