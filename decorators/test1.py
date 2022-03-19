a = 5


def func1():
    b = 2

    def func2():
        c = 3

        def func3():
            print(c)
            print(b)
            print(a)

        return func3

    return func2()


func3 = func1()
func3()  # this interior function has access to all it's exterior variables, this is closure
# closure - a function remembers it's environment
