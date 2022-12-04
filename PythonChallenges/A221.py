import random
list1 = []
list2 = []
for i in range(50):
    r = random.randint(1,25)
    list1.append(r)
print(list1)
def duplicateremover(list1):
    for i in list1:
        if i not in list2:
            list2.append(i)
        print(list2)
    print(list2)

duplicateremover(list1)
