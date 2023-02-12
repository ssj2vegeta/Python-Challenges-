import random
k = random.randint(1,12)
j = random.randint(1,12)
ans = int(input(f"what is {k} * {j}?"))
if ans == k*j:
    print("that is correct, well done")
else:
    print("that is incorrect unfortunately")
