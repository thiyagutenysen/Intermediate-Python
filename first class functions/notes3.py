# You can pass the function as a parameter to another function
# best example is the map function
# inside this function you pass an array and a function
# map takes each value from the array and passes it into the function

# instead of using the builtin map function let's create our own map function inorder to understand
def my_map(function, array):
    ans = []
    for i in array:
        ans.append(function(i))
    return ans


def function(x):
    return x * x


array = [1, 2, 3, 4, 5]

print(my_map(function, array))
