while True:
    devious = input("please enter a float")
    if "." in devious:
        try:
            devious = float(devious)
        except ValueError:
            print("not a float")
            continue
        print("valid input")
        break
    else:
        raise Exception("not a float bro")
    
print(devious)
