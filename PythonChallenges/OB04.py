masterlist = []
number = []
forename = []
surname = []
position = []
ci = []
fi = []
with open("cutecats.txt", "r") as file:
    for i in file:
        count = 0
        for i in file:
            if count == 0:
                number.append(i.strip())
                count += 1
                continue
            elif count == 1:
                forename.append(i.strip())
                count += 1
                continue
            elif count == 2:
                surname.append(i.strip())
                count += 1
                continue
            elif count == 3:
                position.append(i.strip())
                count += 1
                continue
            elif count == 4:
                ci.append((i.strip()))
                count += 1
                continue
            elif count == 5:
                fi.append(i.strip())
                count = 0
                continue
print(number)
for i in ci:
    i = float(i)


for i in range(len(ci)):
    print(number[i], forename[i], surname[i], position[i], ci[i], fi[i])

n = len(ci)
for i in range(n-1):
    for j in range(n-i-1):
        if ci[j] > ci[j + 1] :
            ci[j], ci[j+1] = ci[j+1], ci[j]
            number[j], number[j+1] = number[j+1], number[j]

for i in range(len(ci)):
    print(number[i])
