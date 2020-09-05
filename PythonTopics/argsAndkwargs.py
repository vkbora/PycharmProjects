# *args

def sum(*args):
    s = 0
    for i in args:
        s += i
    print(s)


sum(12, 12, 12)


def add(a, b, c):
    print(a, b, c)


args = [1, 2, 3]

add(*args)


# **kwargs

def mul(a, b, c):
    print(a, b, c)


aa = {"a": "one", "b": "two", "c": 10}

mul(**aa)


def div(**kwargs):
    for i, j in kwargs.items():
        print(i, j)


div(name="tom", sport="football", height=10)
