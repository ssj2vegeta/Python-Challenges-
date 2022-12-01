import random
list1 = ["rock","paper","scissors"]
while True:
    print(list1)
    input1 = input("please input either rock paper or sciessors")
    if input1 not in list1:
        print("invalid input")
        continue
    else:
        break
randomised = random.choice(list1)
if input1 == "rock":
    if randomised == "paper":
        print(f"the ai chose {randomised}")
        print("you lose!")
    elif randomised == "scissors":
        print(f"the ai chose {randomised}")
        print("you win!")
    else:
        print("draw!")
elif input1 == "scissors":
    if randomised == "rock":
        print(f"the ai chose {randomised}")
        print("you lose!")
    elif randomised == "paper":
        print(f"the ai chose {randomised}")
        print("you win!")
    else:
        print("draw!")
if input1 == "paper":
    if randomised == "scissors":
        print(f"the ai chose {randomised}")
        print("you lose!")
    elif randomised == "rock":
        print(f"the ai chose {randomised}")
        print("you win!")
    else:
        print("draw!")
