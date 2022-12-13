import random
floors = int(input('how many floors do you want?'))
listoffloors = []
for i in range(floors):
    listoffloors.append(i)

print(listoffloors)

for i in range(floors):
    d = random.choice(listoffloors)
    listoffloors.remove(d)
    print(f"security guards have visited this floor: {d}")
