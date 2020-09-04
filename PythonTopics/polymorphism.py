#  Overriding variable and Method

class Parent:
    name = "vicky"


class Child(Parent):
    name = "virendra"


obj = Child()
print(obj.name)


class Bank:
    def roi(self):
        return 0


class ICICI(Bank):
    def roi(self):
        return 10.5


bankObj = ICICI()
print(bankObj.roi())


#  Overloading Method


class Human:
    def hello(self, name=None):
        if name is not None:
            print("Hello " + name)
        else:
            print("No Name")


humanObj = Human()
humanObj.hello("VKB")
humanObj.hello()


class Bird:
    def fly(self, name=None):
        if name == "parot":
            print("Can fly")
        if name == "penguin":
            print("Cant fly")
        if name is None:
            print("No Input")


birdObj = Bird()
birdObj.fly("penguin")
birdObj.fly("parot")
birdObj.fly()


