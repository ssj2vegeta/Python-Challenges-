import random
k = random.randint(1,111)

a = 1
d = 111
guesses = 0
count = 0
while True:
    guess = random.randint(a, d)
    if guess > k:
        guesses += 1
        d = guess
        continue
    elif guess < k:
        guesses += 1
        a = guess
        continue
    elif guess == k:
        guesses += 1
        break

print(f"this took {guesses} guesses")
