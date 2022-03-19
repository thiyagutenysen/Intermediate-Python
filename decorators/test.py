a = 5


def func1():
    b = 2

    def func2():
        print(b)
        print(a)

    return func2


b = 3
func2 = func1()
func2()  # this func2 has access to it's outer function's variable, which is b
# it also has access to global variable which is a

