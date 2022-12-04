p1score = 0
p2score = 0
while True:
    print("its player one's turn to ask ")
    p1question = input("enter your question")
    p1answer = input("enter answer to question")
    p1answer = p1answer.strip().lower()
    print(p1question)
    print("its player two's turn to guess")
    p2guess = input("enter your guess")
    p2guess = p2guess.strip().lower()
    if p2guess == p1answer:
        print("guess is corrent!")
        p2score += 1
    elif p2guess != p1answer:
        print(f"guess is incorrect - ans is: {p1answer}")
    print("its player two's turn to ask ")
    p2question = input("enter your question")
    p2answer = input("enter answer to question")
    p2answer = p2answer.strip().lower()
    print(p2question)
    print("its player ones's turn to ask")
    p1guess = input("enter your guess")
    p1guess = p1guess.strip().lower()
    if p1guess == p2answer:
        print("guess is corrent!")
        p1score += 1
    elif p1guess != p2answer:
        print(f"guess is incorrect - ans is: {p2answer}")
    print(f"the current score is {p1score} for player 1 and {p2score} for player 2")
    playagain = input("play again?")
    if playagain == "yes":
        continue
    else:
        break
