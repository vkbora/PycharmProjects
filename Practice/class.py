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
    print(aa + bb)      # first method access global variables

    def add(self, x, y):  # Local Variables
        print(self.a + self.b)
        print(x + y)
        print(globals()['aa'] + globals()['bb'])      # second method access global variables


c4 = MyClass4()
c4.add(2000, 2000)


