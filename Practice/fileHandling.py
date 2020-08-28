# Write Data
file = open("C://Users//vkbora//PycharmProjects//Practice//textfile", "w")
file.write("Hi \n")
file.write("Vicky")
print("Written Successfully")
file.close()

# Read Data
file = open("C://Users//vkbora//PycharmProjects//Practice//textfile", "r")
readdata = file.read()
print(readdata)
file.close()

file = open("C://Users//vkbora//PycharmProjects//Practice//textfile", "r")
readdata1  = file.read(3)
print(readdata1)
file.close()

file = open("C://Users//vkbora//PycharmProjects//Practice//textfile", "r")
readdata2 = file.readlines()
print(readdata2)
file.close()

file = open("C://Users//vkbora//PycharmProjects//Practice//textfile", "r")
readdata3 = file.readline()
print(readdata3)
file.close()

# Append Line
file = open("C://Users//vkbora//PycharmProjects//Practice//textfile", "a")
file.write("\nHello Virendra")
print("Append Successfully\n")
file.close()

file = open("C://Users//vkbora//PycharmProjects//Practice//textfile", "r")
for x in file:
    print(x, end="")
file.close()

