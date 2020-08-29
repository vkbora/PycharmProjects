from itertools import product

name = "John"
age = 25
sal = 10000.46

# using variables name
print(name, age, sal)

# using details info of variables
print("Name is :", name, ", Age is :", age, ", Sal is :", sal)

print("Name is : ", name)
print("Age is : ", age)
print("Sal is : ", sal)

# Using Data Type of variables
print("Name: %s, Age: %d, Salary: %g" % (name, age, sal))

# Using {} and format method
print("Name: {}, Age: {}, Salary: {}".format(name, age, sal))

# Using {index value} and format method
print("Name: {0}, Age: {1}, Salary: {2}".format(name, age, sal))
