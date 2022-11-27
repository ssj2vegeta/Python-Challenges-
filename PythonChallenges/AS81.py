import random
randomlist = []
for i in range(20):
    r = random.randint(1,20)
    randomlist.append(r)
total = 1
for i in randomlist:
    total = total * i
print(total)
print(sum(randomlist))
