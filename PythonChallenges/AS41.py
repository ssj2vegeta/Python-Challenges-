bitlist = ["0","1"]
bit = ""
paritybit = ""
emptlist  = []
parity = input("what parity would you like to use")
while True:
    bit = (input("please enter your bit (7 digits)"))
    integer = int(bit)
    if len(bit) == 7:
        for i in bit:
            if i not in bitlist:
                print("A BIT CAN ONLY HAVE 0 or 1")
                break
            else:
                continue
    else:
        print("7 digits only!!")
        continue
    break
while True:
    paritybit = (input("please enter your paritybit (1 digit)"))
    integer1 = int(bit)
    if len(paritybit) == 1:
        for i in bit:
            if i not in bitlist:
                print("A BIT CAN ONLY HAVE 0 or 1")
                break
            else:
                continue
    else:
        print("1 digit only!!")
        continue
    break

for i in bit:
    if i == "0":
        emptlist.append(0)
    elif i == "1":
        emptlist.append(1)
for i in paritybit:
    if i == "0":
        emptlist.append(0)
    elif i == "1":
        emptlist.append(1)


if parity == "odd":
    if sum(emptlist) % 2 != 0:
        print("valid byte")
        print(emptlist)
    elif sum(emptlist) % 2 == 0:
        print("invalid byte")
        emptlist.pop(7)
        emptlist.append(1)
        print(f"the corrected byte is {emptlist}")
if parity == "even":
    if sum(emptlist) % 2 == 0:
        print("valid byte")
        print(emptlist)
    elif sum(emptlist) % 2 != 0:
        print("invalid byte")
        emptlist.pop(7)
        emptlist.append(1)
        print(f"the corrected byte is {emptlist}")
