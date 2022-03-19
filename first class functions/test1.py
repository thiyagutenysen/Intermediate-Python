# function name is also treated as a variable
def function():
    return "ahahahahahahahah"


function = 5
print(function)  # output --> 5
print(function())  # output --> TypeError: 'int' object is not callable
