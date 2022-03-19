# Inorder to understand closures, we first need to understand closures

# Closure Definition 1:
# A closure is the combination of a function bundled together (enclosed),
# with references to its surrounding state (the lexical environment).
# In other words, a closure gives you access to an outer function's scope from an inner function

# Closure Definition 2:
# JavaScript variables can belong to the local or global scope.
# Global variables can be made local (private) with closures.

# Closure Definition 3:
# Closures are functions that refer to independent (free) variables.
# In other words, the function defined in the closure ‘remembers’ the environment in which it was created.

# example 1
def function1():
    message = "hello mac"

    def function2():
        print(message)

    return function2


# Method 1
function2 = function1()
function2()  # here function 2 will be able to use the variable "message" that's defined inside function1, this is closure

# Method 2
function1()()  # it's the same thing
print("-----------------------------------------------")

# Closure My definition:
# Closure is that an inner function that remembers and has access to variables in the local scope in which it is created,
# even after the outer function has completed execution

# example 2
def function1(message):
    def function2():
        print(message)

    return function2


function21 = function1("hello mac")
function22 = function1("hello sweet dee")
function21()  # this inner function remembers it's own outer function variable
function22()  # this inner function remembers it's own outer function variable
print("-----------------------------------------------")

# Closure Wise and Poetic Definition:
# A Closure closes over a free variables from their environment

# example 3
def html_tag(tag):
    # function within a function
    def wrap_text(message):
        print("<{0}>{1}</{0}>".format(tag, message))

    return wrap_text


html_line = html_tag("h1")
print(html_line)
html_line("Title headline")
