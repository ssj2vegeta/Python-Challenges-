import random
masterdict = {"Goku": 500, "Vegeta": 550, "Piccolo": 450, "Krillin": 220, "Android 18": 430, "Android 17": 480, "Frieza": 600, "Merus":1000,"Beerus":750,"Whis":2500, "Goku Black":495, "Zamasu":460}
player1dict = {}
player2dict = {}

keys = list(masterdict.keys())

while len(player1dict) < 5:
    randomrandom = random.choice(keys)
    player1dict[randomrandom] = masterdict[randomrandom]
while len(player2dict) < 5:
    randomrandom = random.choice(keys)
    player2dict[randomrandom] = masterdict[randomrandom]


while True:
    while True:
        print(player1dict)
        player1input = input("choose one of the keys from your card list")
        try:
            player1dict[player1input]
            break
        except KeyError:
            print("that does not exist in your card deck - please try again")
            continue
    while True:
        print(player2dict)
        player2input = input("choose one of the keys from your card list")
        try:
            player2dict[player2input]
            break
        except KeyError:
            print("that does not exist in your card deck - please try again")
            continue
    if player1dict[player1input] > player2dict[player2input]:
         print("player 1 wins this round !")
         if len(player2dict) > 1:
            del player2dict[player2input]
            continue
         elif len(player2dict) == 1:
            print("player1 wins")
            break
    elif player1dict[player1input] < player2dict[player2input]:
        print("player 1 wins this round !")
        if len(player1dict) > 1:
            del player1dict[player1input]
            continue
        elif len(player1dict) == 1:
            print("player2 wins")
            break
    elif player1dict[player1input] == player2dict[player2input]:
        print("draw!")
        continue
