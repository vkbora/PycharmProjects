
name = "vicks"
print(name)

name = 'vicky'
print(name)

name = str("Hi")
print(name)

str1 = "welcome "
str2 = "welcome"

print("str1: ", id(str1))
print("str2: ", id(str2))

str2 = str2 + "vicky"

print("str1: ", id(str1))
print("str2: ", id(str2))

print(str1 * 5)     # welcome welcome welcome welcome welcome

print(str1[1:3])    # el

print(str1[:6])     # welcom

print(str1[4:])     # ome

print(ord('A'))     # 65,  return ASCII code

print(chr(65))      # A, return ASCII value

str1 = "welcome"

print("length: ", len(str1))

print("max value: ", max(str1))

print("min value: ", min(str1))

print("come" in str1)       # True

print("comee" in str1)      # False

print("comee" not in str1)  # True

print("come" not in str1)   # False

print(str1 == str2)     # False

str3 = "welcome"

print(str1 == str3)     # True

print(str1 != str2)     # True

for i in str1:
    print(i, end="")
print()

for j in str1:
    print(j, end=" ")
print()

for k in str1:
    print(k, end=" doo ")










