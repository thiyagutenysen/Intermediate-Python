# This is important to understand higher order functions, currying and closures

# official definition
# 1. A programming language is said to have First-class functions,
# when functions in that language are treated like any other variable
# 2. In languages with first-class functions, the names of functions do not have any special status;
# they are treated like ordinary variables with a function type.

# In programming language design, a first-class citizen (also type, object, entity, or value)
# in a given programming language is an entity which supports all the operations generally available to other entities.

# Properties of first class functions:
# 1. A function is an instance of the Object type.
# 2. You can store the function in a variable.
# 3. You can pass the function as a parameter to another function.          |
# 4. You can return the function from a function.                           | -----> 3 nad 4 means higher order functions
# 5. You can store them in data structures such as hash tables, lists, …

# Conclusions from my own experimentation
# 1. function name is also treated as a variable, inorder to call the function successfully,
# we should not reinitialize the function name as int or float or string or etc., Checkout test1.py to understand
