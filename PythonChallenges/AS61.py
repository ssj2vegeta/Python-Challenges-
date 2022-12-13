import random
lst = []
scndlst = []
rows = int(input("how many rows do you want?"))
columns = int(input("how many columns do you want?"))
print(lst)
for i in range(rows):
    lst.append([])
for i in lst:
    for k in range(rows):
        k = random.randint(0,50)
        i.append(k)
        scndlst.append(k)
k = max(scndlst)
p = 0
for i in lst:
    o = 0
    for j in i:
        if k == j:
            print(p,o)
            break
        else:
            o += 1
    p += 1
print(k)
print(lst)
