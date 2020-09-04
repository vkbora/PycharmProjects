print("Single inheritance\n")


class MyClassA:
    def m1(self):
        print("This is method one from class A")


class MyClassB(MyClassA):
    def m2(self):
        print("This is method two from class B")


CA = MyClassA()
CA.m1()

CB = MyClassB()
CB.m2()
CB.m1()

print("\nMultilevel inheritance\n")


class MyClassC(MyClassB):
    def m3(self):
        print("This is method three from class C")


CC = MyClassC()
CC.m3()
CC.m2()
CC.m1()

print("\nHierarchical inheritance\n")


class MyClassD(MyClassA):
    def m4(self):
        print("This is method four from class D")


CB = MyClassB()
CB.m2()
CB.m1()

CD = MyClassD()
CD.m4()
CD.m1()

print("\nMultiple inheritance\n")


class MyClassE():
    def m5(self):
        print("This is method five from class E")


class MyClassF(MyClassA, MyClassE):
    def m6(self):
        print("This is method six from class F")


CF = MyClassF()
CF.m6()
CF.m5()
CF.m1()

# Super() keyword
a, b = 10, 20


class SA:
    a, b = 100, 200

    def __init__(self):
        print("This is class SA constructor")

    def m1(self):
        print("This is method one from class SA")


class SB(SA):
    a, b = 1000, 2000

    def __init__(self):
        print("This is class SB constructor")
        super().__init__()  # Parent class constructor
        SA.__init__(self)  # Parent class constructor

    def m1(self, a, b):
        print("This is method one from class SB")
        print(a + b)  # Local Variables
        print(self.a + self.b)  # Child class Variables
        print(super().a + super().b)  # Parent class variables
        print(SA.a + SA.b)  # Parent class variables
        print(globals()["a"] + globals()["b"])  # globals variables

    def m2(self):
        print("This is method two from class SB")
        self.m1(10000, 20000)  # Child class method
        super().m1()  # Parent class method
        SA.m1(self)  # Parent class method


CSB = SB()
CSB.m2()



