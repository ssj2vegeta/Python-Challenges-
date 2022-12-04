foodlist = []
totalcalories = 0
while True:
    food = input("what did you eat?")
    if food == "end day":
        break
    else:
        foodlist.append(food)
    while True:
        try:
            calories = int(input("how many calories does it have?"))
            break
        except ValueError:
            print("thats not an integer, please try again")
            continue
    totalcalories = calories + totalcalories

print(f"total list of food is {foodlist}")
print(f" total calories is {totalcalories}")
