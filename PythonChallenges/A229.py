import random
choice = input("ipv4 or  ipv6?")
if choice == "ipv4":
    number = int(input("pick a number from 1 to 100"))
    masterlist = []
    for i in range(number):
        str = ""
        for i in range(4):
            k = random.randint(1,3)
            for i in range(k):
                numlist = ["1","2","3","4","5","6","7","8","9"]
                d = random.choice(numlist)
                str = str + d
            str = str + "."
        str = str[:len(str)-1]
        masterlist.append(str)
    print(masterlist)
elif choice == "ipv6":
    number = int(input("pick a number from 1 to 100"))
    masterlist = []
    for i in range(number):
        str = ""
        for i in range(8):
            for i in range(4):
                alphlist = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't','u', 'v', 'w', 'x', 'y', 'z','1','2','3','4','5','6','7','8','9']
                random.shuffle(alphlist)
                d = random.choice(alphlist)
                str = str + d
            str = str + ":"
        str = str[:len(str) - 1]
        masterlist.append(str)
    print(masterlist)
