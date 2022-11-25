import random
emptlist = []
emptlist2 = []
for i in range(1,21):
    emptlist.append(i)
print(emptlist)

for i in range(20):
    k = random.choice(emptlist)
    emptlist2.append(k)
    emptlist.remove(k)

print(emptlist2)

for i in emptlist2:
    if i % 3 == 0 and i % 5 == 0:
        print("FIZZBUZZ")
    elif i % 3 == 0:
        print("FIZZ")
    elif i % 5 == 0:
        print("BUZZ")
    else:
        print(i)
