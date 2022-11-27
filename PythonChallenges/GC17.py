while True:
    isbn = input("enter your isbn")
    isbn = isbn.strip()
    if len(isbn) < 10 or len(isbn) > 10:
        print("thats not 10 digits")
    else:
        break
isbnlist = []
for i in isbn:
    isbnlist.append(int(i))
print(isbnlist)

def isbncalculator():
    k = 10
    result = 0
    for i in range(9):
        result =  result + (isbnlist[i] * k)
        k -= 1
    lastdigit = 11 - (result % 11)
    if lastdigit == isbnlist[9]:
        return "isbn is valid"
    else:
        return "isbn is invalid"

print(isbncalculator())
