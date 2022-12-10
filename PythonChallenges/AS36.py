import random

list1 = []

for i in range(100):
    d = random.randint(1,1000)
    list1.append(d)
finallist = [list1[0],list1[-1]]
print(list1)
print(finallist)
