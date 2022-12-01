input1 = input("jokes shop jokes shop ")
empt = ""
for i in range(len(input1)-1,-1,-1):
    empt = empt + input1[i]

print(empt)
