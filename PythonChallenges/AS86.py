import secrets
list1 = []
with open("promptspal.txt", "r") as random:
    for i in random:
        list1.append(i.strip())
print(secrets.choice(list1))
