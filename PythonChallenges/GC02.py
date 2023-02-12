input1 = ("am or pm?")
hour = input("hour?")
minute = input("minute?")
second = input("second")
if input1 == "am":
    print(f"{hour}:{minute}:{second}")
elif input1 == "pm":
    print(f"{hour + 12}:{minute}:{second}")
