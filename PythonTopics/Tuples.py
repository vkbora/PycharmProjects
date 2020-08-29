t1 = tuple("abx")
print(t1)

t2 = (11, 22, 33)
print(t2)

t3 = ([1, 2, 3, 4])
print(t3)

t4 = (1, 12, 15, 44)
print(min(t4))
print(max(t4))
print(len(t4))

for i in t4:
    print(i, end=" ")
print()

print(t4[2:4])
print(t4[:4])
print(t4[1:])

print(12 in t4)
print(22 not in t4)

