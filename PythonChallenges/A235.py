import random
def nqueens(cells):
    list1 = []
    for i in range(cells):
        list1.append([])
    for i in list1:
        for j in range(cells):
            i.append("")
    k = random.randint(0, cells - 1)
    j = random.randint(0, cells - 1)
    list1[k][j] = "queen"
    for i in list1:
        print(i)
    print()
    count = 1
    counter = 0
    while count < cells:
        counter += 1
        breakcounter = 0
        k = random.randint(0, cells - 1)
        j = random.randint(0, cells - 1)
        for i in range(0,cells):
            if list1[i][j] == "queen":
                breakcounter += 1
                break
            if list1[k][i] == "queen":
                breakcounter += 1
                break
            if k + i < (cells-1) and j + i < (cells-1):
                if list1[k+i][j+i] == "queen":
                    breakcounter += 1
                    break
            if k - i > (-1) and j + i < (cells - 1):
                if list1[k-i][j+i] == "queen":
                    breakcounter += 1
                    break
            if k - i > (-1) and j - i > (-1):
                if list1[k-i][j-i] == "queen":
                    breakcounter += 1
                    break
            if j - i > (-1) and k + i < (cells - 1):
                if list1[k + i][j - i] == "queen":
                    breakcounter += 1
                    break
        if counter > 4 ** cells:
            print(f"it is not possible to place {cells} number of queens")
            break
        if breakcounter == 1:
            continue
        elif breakcounter == 0:
            list1[k][j] = "queen"
            count += 1
    if count == cells:
        for i in list1:
            print(i)
    elif count != cells:
        return False
