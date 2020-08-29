dic = dict({1: "one", 2: "two", 3: "three"})
print(dic)

dic1 = {"one": 1, "two": 2, "three": 3}
print(dic1)

print(dic[1])
print(dic1["one"])

dic[4] = "four"
print(dic)

dic[1] = "one1"
print(dic)

del dic[1]
print(dic)

for x in dic:
    print(x, ":", dic[x], end=" ")
print()

print(len(dic))

print(dic == dic1)
print(dic != dic1)

dic2 = dic.copy()
print(dic2)

print(dic == dic2)
print(dic != dic2)

dic.popitem()
print(dic)

dic.clear()
print(dic)

print(dic1.keys())
print(dic1.values())

print(dic1.get("one"))

dic1.pop("one")
print(dic1)

dic1.popitem()
print(dic1)









