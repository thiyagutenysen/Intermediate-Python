# You can store the function in a variable
def square(x):
    return x * x


y = square  # if we use the parathesis then it means executing the function, so we don't put () here

print(y)
print(square)
print(y(5), square(5))
