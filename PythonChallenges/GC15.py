k = 1
for i in range(9):
    for i in range(1,k+1):
        print(i,end ="")
    for i in range(k-1,0,-1):
        print(i, end="")
    print("")
    k += 1
k -= 2
for i in range(8):
    for i in range(1,k+1):
        print(i,end ="")
    for i in range(k-1,0,-1):
        print(i, end="")
    print("")
    k -= 1
