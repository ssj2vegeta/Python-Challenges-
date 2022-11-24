j = 1 - 1
for i in range(101, 1000):
    string = str(i)
    list1 = list(string)
    for k in list1:
        list2 = []
        integer = int(k)
        list2.append(integer)
        list1 = list1 + list2
    list1 = list1[3:]
    if i % sum(list1) == 0:
        j += 1
print(f"the number of numbers that are nice is {j}")
