import random
L = []
Lsorted = []
for i in range(9):
    k = random.randint(1,50)
    L.append(k)
print(L)
for i in range(1,len(L)):
    j = L[i]
    while L[i-1] > j and i > 0:
        L[i], L[i-1] = L[i-1],L[i]
        i -= 1
print(L)
