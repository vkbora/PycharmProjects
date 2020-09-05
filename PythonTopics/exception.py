print("Programm is started")

try:
    print(10 / 0)  # ZeroDivisionError: division by zero
except ZeroDivisionError:
    print("Zero Division Error Handled")
except TypeError:
    print("Type Error Handled")
else:
    print("else block handled")
finally:
    print("finally block handled")

print("Program is completed")


def age(age):
    if age < 0:
        raise ValueError("enter the +ve number")
    else:
        print("age is : ", age)


try:
    age(-2)
except ValueError as ex:
    print("Exception is : ", ex)


