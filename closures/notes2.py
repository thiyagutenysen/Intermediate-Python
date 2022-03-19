# complex example for closures
import logging

logging.basicConfig(filename="example.log", level=logging.INFO)

# this logger function takes another function as argument
def logger(func):
    def log_func(*args):
        # this log_func can use it's outer function argument "func". We use it to get the function name as func.__name__
        # the below line is an example for closure, as it uses func
        logging.info('Running "{}" with arguments {}'.format(func.__name__, args))
        # the below line is an example for closure as we can access func from it's outer function
        # **the below line is also an example for first-class function as it can be used as variable too
        print(func(*args))

    return log_func


def add(x, y):
    return x + y


def sub(x, y):
    return x - y


add_logger = logger(add)
sub_logger = logger(sub)

add_logger(3, 3)
add_logger(4, 5)
