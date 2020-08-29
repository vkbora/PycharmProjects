def myfunc():
    pass


myfunc()


def sum(start, end):
    result = 0
    for i in range(start, end + 1):
        result = result + i
    print(result)


sum(10, 20)


def test():
    i = 100
    return


print(test())

xy = 100  # global variable


def cool():
    xy = 200  # local variable
    print(xy)


cool()  # 200

print(xy)  # 100
