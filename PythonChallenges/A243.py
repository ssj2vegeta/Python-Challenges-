def positiveinteger():
    while True:
        try:
            input1 = int(input("please enter a positive integer"))
            if input1 < 0:
                print("thats not a positive integer")
                continue
            else:
                break
        except (EOFError, ValueError) as error:
            print("that is not an integer")
            continue
positiveinteger()
