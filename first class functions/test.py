def func(array):
    for i, val in enumerate(array):
        array[i] = val - 1
    return array


array = [1, 2, 3, 4, 5]
print(func(array))
print(array)


def funct(val):
    val = val - 1
    return val


val = 5
print(funct(val))
print(val)

# only objects stays the same, others are copied and modified separately
# objects once modified are everywhere modified
