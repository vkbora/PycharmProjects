from abc import abstractmethod, ABC


class Animal(ABC):

    @abstractmethod
    def eat(self):
        pass


class Tiger(Animal):
    def eat(self):
        print("eat food")


class Cow(Animal):
    def eat(self):
        print("eat grass")


t = Tiger()
t.eat()

c = Cow()
c.eat()


class X(ABC):

    @abstractmethod
    def m1(self):
        pass

    @abstractmethod
    def m2(self):
        pass


class Y(X):
    def m1(self):
        print("This is method one")


class Z(Y):
    def m2(self):
        print("This is method two")


dd = Z()
dd.m1()
dd.m2()


class Cal(ABC):

    def __init__(self, val):
        self.value = val

    def sub(self):
        print("This non abstract method")

    @abstractmethod
    def add(self):
        pass


class C(Cal):
    def add(self):
        print(self.value + 100)


cc = C(200)
cc.add()
cc.sub()
