list1 = list()
print(list1)

list2 = list([22, 11, 55, 2])
print(list2)

list3 = list(["tom", 33, "jerry"])
print(list3)

list4 = list("AB")
print(list4)

lst = [1, 2, 3, 4, 50]
print(lst)
print(lst[0])
print(lst[2])

print(2 in lst)  # TRUE
print(4 not in lst)  # TRUE

print(len(lst))
print(min(lst))
print(max(lst))
print(sum(lst))

print(lst[1:2])
print(lst[:4])
print(lst[2:])

print(lst + lst)
print(lst * 3)

for i in lst:
    print(i, end=" ")
print()

lst.append(2)
lst.append(2)
print(lst)

print(lst.count(2))
lst.extend(list2)
print(lst)
print(lst.index(2))

lst.insert(1, 22)
print(lst)

lst.pop(2)  # delete 2 position value
lst.pop()  # delete last value
print(lst)

lst.remove(11)
print(lst)

lst.reverse()
print(lst)

lst.sort()
print(lst)

listfor = [x + 1 for x in range(10)]
print(listfor)

listeven = [x for x in range(1, 22) if x % 2 == 0]
print(listeven)

