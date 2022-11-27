receiver = input("check if your code has qwerty or not!")
list = receiver.split()
empt = ""
for i in list:
    for j in i:
       empt = empt + j #added this to account for spaces
print(empt)
if "qwerty" in empt:
    print("qwerty detected!")
else:
    print("qwerty not detected")
