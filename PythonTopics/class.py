class MyClass1:
    def myfunc(self):
        pass

    def display(self, name):
        print("Name is : ", name)


c1 = MyClass1()
c1.myfunc()
c1.display("vkb")


class MyClass2:
    def m1(self):
        print("instance")

    @staticmethod
    def m2():
        print("static")


c2 = MyClass2()
c2.m1()
MyClass2.m2()


class MyClass3:
    a, b = 100, 120  # class variables

    def add(self):
        print(self.a + self.b)


c3 = MyClass3()
c3.add()

aa, bb = 10, 20  # global variables


class MyClass4:
    a, b = 100, 200  # Class Variables
    print(aa + bb)  # first method access global variables

    def add(self, x, y):  # Local Variables
        print(self.a + self.b)
        print(x + y)
        print(globals()['aa'] + globals()['bb'])  # second method access global variables


c4 = MyClass4()
c4.add(2000, 2000)


class MyClass5:
    def m1(self):
        print("This is method")

    def __init__(self):
        print("This is constructor")


c5 = MyClass5()
c5.m1()


class MyClass6:
    def __init__(self, val1, val2):
        self.val2 = val2
        self.val1 = val1

    def add(self):
        print(self.val1 + self.val2)


c6 = MyClass6(1000, 2000)
c6.add()


class MyClass7:
    def m1(self):
        print("This is method one : No arguments")
        self.m2(100)

    def m2(self, a):
        print("This is method two : ", a)


c7 = MyClass7()
c7.m1()


class MyClass8:
    def __init__(self, name):
        print(name)


c8 = MyClass8("VKB")


class Emp:
    def __init__(self, eid, ename, sal):
        self.eid = eid
        self.ename = ename
        self.sal = sal

    def __str__(self):
        return "eid: {}, ename: {}, sal: {}".format(self.eid, self.ename, self.sal) + "\n" + \
               "eid: %d, ename: %s, sal: %g" % (self.eid, self.ename, self.sal)


emp = Emp(122, "VKB", 100000)
print(emp)


class MyClass9:
    def __str__(self):
        return "Welcome"

    def __del__(self):
        print("Deleted")


c9 = MyClass9()
print(c9)

