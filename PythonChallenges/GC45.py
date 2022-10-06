x = 2
while x == 2:
    xinput = input("please type one character here ")
    if len(xinput) < 2:
        print("thank you")
        x -= 1
    if len(xinput) > 1:
        print("thats more than one character - please try again")
