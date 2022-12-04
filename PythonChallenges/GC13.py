ISBN = (input("please input your ISBN"))
def ISBNFUNCTION(ISBN):
    isbnlist = [1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3]
    while True:
        try:
            INTISBN = int(ISBN)
        except ValueError:
            print("please enter an integer")
            raise Exception("valuerror")
        if len(ISBN) != 13:
            print("isbn doesnt have a length of 13")
            raise Exception("lengtherror")
        else:
            break
    total = 0
    for i in range(0,len(isbnlist)):
        total = total + isbnlist[i] * int(ISBN[i])
    remainder = total % 10
    if remainder == 0:
        if remainder == int(ISBN[12]):
            return "ISBN is Valid"
        else:
            return "ISBN is Invalid"
    elif remainder != 0:
        remainder = 10 - remainder
        if remainder == int(ISBN[12]):
            return "ISBN is Valid"
        else:
            return "ISBN is Invalid"
print(ISBNFUNCTION(ISBN))
