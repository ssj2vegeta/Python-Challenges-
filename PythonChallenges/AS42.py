listofcharacters = {"goku" : {"Health" : 500, "Kamehameha": 200, "Solar Flare": 15}, "vegeta"  : {"Health": 550, "Final Flash": 220, "Rush Attack":100} }
player1 = listofcharacters["goku"]
player2 = listofcharacters["vegeta"]
print("player1 is goku and player2 is vegeta")
solarflarecooldown = 0
while True:
    if solarflarecooldown > 0:
        solarflarecooldown -= 1
    solarflare = 0
    print(player1)
    input1 = input("These are your current moves and your current health. pick a move to use")
    if input1 == "Health":
        print("You cannot use your health as a move! You lost your turn!")
    elif input1 == 'Solar Flare':
        if solarflarecooldown == 0:
            solarflare += 1
            player2["Health"] -= player1[input1]
            solarflarecooldown += 2
        else:
            print("Solar Flare requires a cooldown")
    else:
        player2["Health"] -= player1[input1]
    if solarflare > 0:
        print("Goku used Solar Flare! Vegeta has been blinded and cannot attack!")
        continue
    print(player2)
    input2 = input("These are your current moves and your current health. pick a move to use")
    if input2 == "Health":
        print("You cannot use your health as a move! You lost your turn!")
    else:
        player1["Health"] -= player2[input2]
    if player1["Health"] < 0:
        print("Vegeta has won!")
        break
    if player2["Health"] < 0:
            print("Goku has won!")
            break
