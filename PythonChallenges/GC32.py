import random

list1 = ["silent", "confess"]
print("user is prisonerA and this computer is prisonerB")
while True:
    confession = input("do you stay silent or confess?")
    computerchoice = random.choice(list1)
    print(f"the computer has chosen {computerchoice}")
    if confession == "silent":
        if computerchoice == "silent":
            print("both prisoners are in prison for a year")
        elif computerchoice == "confess":
            print("prisonerB is out of prison but prisonerA is in prison for 20 years!!!")
    elif confession == "confess":
        if computerchoice == "silent":
            print("prisonerA is out of prison but prisonerB is in prison for 20 years!!!")
        elif computerchoice == "confess":
            print("both prisoenrs are in jail for 5 years")
    else:
        print("invalid input")
        continue
    prompt = input("do you want to play again?")
    if prompt == "yes":
        continue
    else:
        break
