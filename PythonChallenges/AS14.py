str = input("input test string")
count = 0
for i in str:
    if i == "(":
        count += 1
    elif i == ")":
        count -= 1
    else:
        continue
if count == 0:
    print("valid!")
else:
    print("invalid")
