player1list = []
player2list = []

with open("poker.txt","r") as file:
    for i in file:
        split = i.split()
        player1list.append(split[0:5])
        player2list.append(split[5:10])
def maxsort(list1, list2):
    while True:
        k = max(list1)
        m = max(list2)
        if k == m:
            list1.remove(k)
            list2.remove(m)
            continue
        elif k > m:
            return True
        elif m > k:
            return False


def pokersort(list1):
    while True:
        count = 0
        if "K" in list1:
            list1.remove("K")
            list1.append(13)
            count += 1
        if count < 1:
            break
        else:
            continue
    while True:
        count = 0
        if "T" in list1:
            list1.remove("T")
            list1.append(10)
            count += 1
        if count < 1:
            break
        else:
            continue
    while True:
        count = 0
        if "J" in list1:
            list1.remove("J")
            list1.append(11)
            count += 1
        if count < 1:
            break
        else:
            continue
    while True:
        count = 0
        if "Q" in list1:
            list1.remove("Q")
            list1.append(12)
            count += 1
        if count < 1:
            break
        else:
            continue
    while True:
        count = 0
        if "A" in list1:
            list1.remove("A")
            list1.append(14)
            count += 1
        if count < 1:
            break
        else:
            continue
    for i in range(len(list1)):
        list1[i] = int(list1[i])
    list1.sort()
    return list1




scoringlist = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]

player1count = 0
player2count = 0
scorelist1 = []
scorelist2 = []
for i in range(1000):
    counter1 = 0
    counter2 = 0
    royalflushlist = ["T", "J", "Q", "K", "A"]
    templist1 = []
    templist2 = []
    countlist = []
    dv = 0
    for j in player1list[i]:
        if j[0] in royalflushlist:
            royalflushlist.remove(j[0])
        else:
            continue
    if len(royalflushlist) == 0:
        counter1 += 10
    royalflushlist = ["T", "J", "Q", "K", "A"]
    # -
    templist1 = []
    templist2 = []
    countlist = []
    dv = 0
    for j in player2list[i]:
        if j[0] in royalflushlist:
            royalflushlist.remove(j[0])
        else:
            continue
    if len(royalflushlist) == 0:
        counter2 += 10
    templist1 = []
    templist2 = []
    countlist = []
    dv = 0
    for j in player1list[i]:
        templist1.append(j[0])
    for j in player2list[i]:
        templist2.append(j[0])
    if counter1 > counter2 or counter2 > counter1:
        scorelist1.append(counter1)
        scorelist2.append(counter2)
        continue
    elif counter2 == counter1 and counter2 != 0 and counter1 != 0:
        if maxsort(pokersort(templist1), pokersort(templist2)) == True:
            counter1 += 1
            scorelist1.append(counter1)
            scorelist2.append(counter2)
            continue
        elif maxsort(pokersort(templist1), pokersort(templist2)) == False:
            counter2 += 1
            scorelist1.append(counter1)
            scorelist2.append(counter2)
            continue
    # --
    templist1 = []
    templist2 = []
    countlist = []
    dv = 0
    for j in player1list[i]:
        templist1.append(j[1])
    scount = 0
    for j in templist1:
        if j == templist1[1]:
            scount += 1
    for j in player1list[i]:
        templist2.append(j[0])
    sorteddlist = pokersort(templist2)
    for j in range(len(templist2)):
        if sorteddlist[0] + j == sorteddlist[j]:
            dv += 1
            continue
        elif sorteddlist[0] + j != sorteddlist[j]:
            continue
    if dv == len(sorteddlist) and scount == len(templist1):
        counter1 = counter1 + 9 + float(sorteddlist[0] / 10)
    # -
    templist1 = []
    templist2 = []
    countlist = []
    dv = 0
    for j in player2list[i]:
        templist1.append(j[1])
    scount = 0
    for j in templist1:
        if j == templist1[1]:
            scount += 1
    for j in player2list[i]:
        templist2.append(j[0])
    sorteddlist = pokersort(templist2)
    for j in range(len(templist2)):
        if sorteddlist[0] + j == sorteddlist[j]:
            dv += 1
            continue
        elif sorteddlist[0] + j != sorteddlist[j]:
            continue
    if dv == len(sorteddlist) and scount == len(templist1):
        counter2 = counter2 + 9 + float(sorteddlist[0] / 10)
    templist1 = []
    templist2 = []
    countlist = []
    dv = 0
    for j in player1list[i]:
        templist1.append(j[0])
    for j in player2list[i]:
        templist2.append(j[0])
    if counter1 > counter2 or counter2 > counter1:
        scorelist1.append(counter1)
        scorelist2.append(counter2)
        continue
    elif counter2 == counter1 and counter2 != 0 and counter1 != 0:
        if maxsort(pokersort(templist1), pokersort(templist2)) == True:
            counter1 += 1
            scorelist1.append(counter1)
            scorelist2.append(counter2)
            continue
        elif maxsort(pokersort(templist1), pokersort(templist2)) == False:
            counter2 += 1
            scorelist1.append(counter1)
            scorelist2.append(counter2)
            continue
    # --
    templist1 = []
    templist2 = []
    countlist = []
    dv = 0
    for j in player1list[i]:
        templist1.append(j[0])
    for j in templist1:
        countd = 0
        for k in templist1:
            if k == j:
                countd += 1
        countlist.append(countd)
        if countd == 4:
            dv += 1
        else:
            continue
    if dv > 0:
        for k in range(0,len(countlist)):
            if countlist[k] == 4:
                for j in range(len(scoringlist)):
                    if templist1[k] == scoringlist[j]:
                        counter1 = counter1 + 8 + float(j / 10)
                        break
                    else:
                        continue
    # -
    templist1 = []
    templist2 = []
    countlist = []
    dv = 0
    for j in player2list[i]:
        templist1.append(j[0])
    for j in templist1:
        countd = 0
        for k in templist1:
            if k == j:
                countd += 1
        countlist.append(countd)
        if countd == 4:
            dv += 1
        else:
            continue
    if dv > 0:
        for k in range(0, len(countlist)):
            if countlist[k] == 4:
                for j in range(len(scoringlist)):
                    if templist1[k] == scoringlist[j]:
                        counter2 = counter2 + 8 + float(j / 10)
                        break
                    else:
                        continue
    templist1 = []
    templist2 = []
    countlist = []
    dv = 0
    for j in player1list[i]:
        templist1.append(j[0])
    for j in player2list[i]:
        templist2.append(j[0])
    if counter1 > counter2 or counter2 > counter1:
        scorelist1.append(counter1)
        scorelist2.append(counter2)
        continue
    elif counter2 == counter1 and counter2 != 0 and counter1 != 0:
        if maxsort(pokersort(templist1), pokersort(templist2)) == True:
            counter1 += 1
            scorelist1.append(counter1)
            scorelist2.append(counter2)
            continue
        elif maxsort(pokersort(templist1), pokersort(templist2)) == False:
            counter2 += 1
            scorelist1.append(counter1)
            scorelist2.append(counter2)
            continue
    # --
    templist1 = []
    templist2 = []
    countlist = []
    dv = 0
    for j in player1list[i]:
        templist1.append(j[0])
    for j in templist1:
        countr1 = 0
        for k in templist1:
            if k == j:
                countr1 += 1
        countlist.append(countr1)
    if 3 in countlist and 2 in countlist:
        for k in range(len(countlist)):
            if countlist[k] == 3:
                for j in range(len(scoringlist)):
                    if templist1[k] == scoringlist[j]:
                        counter1 = counter1 + 7 + float(j / 10)
                        break
                    else:
                        continue
    # -
    templist1 = []
    templist2 = []
    countlist = []
    dv = 0
    for j in player2list[i]:
        templist1.append(j[0])
    for j in templist1:
        countr1 = 0
        for k in templist1:
            if k == j:
                countr1 += 1
        countlist.append(countr1)
    if 3 in countlist and 2 in countlist:
        for k in range(len(countlist)):
            if countlist[k] == 3:
                for j in range(len(scoringlist)):
                    if templist1[k] == scoringlist[j]:
                        counter2 = counter2 + 7 + float(j / 10)
                        break
                    else:
                        continue
    templist1 = []
    templist2 = []
    countlist = []
    dv = 0
    for j in player1list[i]:
        templist1.append(j[0])
    for j in player2list[i]:
        templist2.append(j[0])
    if counter1 > counter2 or counter2 > counter1:
        scorelist1.append(counter1)
        scorelist2.append(counter2)
        continue
    elif counter2 == counter1 and counter2 != 0 and counter1 != 0:
        if maxsort(pokersort(templist1), pokersort(templist2)) == True:
            counter1 += 1
            scorelist1.append(counter1)
            scorelist2.append(counter2)
            continue
        elif maxsort(pokersort(templist1), pokersort(templist2)) == False:
            counter2 += 1
            scorelist1.append(counter1)
            scorelist2.append(counter2)
            continue
    # --
    templist1 = []
    templist2 = []
    countlist = []
    dv = 0
    for j in player1list[i]:
        templist1.append(j[1])
    for j in templist1:
        countd = 0
        for k in templist1:
            if j == k:
                countd += 1
        if countd == 5:
            dv += 1
            countlist.append(countd)
        else:
            continue
    if dv > 0:
        counter1 = counter1 + 6
    templist1 = []
    templist2 = []
    countlist = []
    dv = 0
    for j in player2list[i]:
        templist1.append(j[1])
    for j in templist1:
        countd = 0
        for k in templist1:
            if j == k:
                countd += 1
        if countd == 5:
            dv += 1
            countlist.append(countd)
        else:
            continue
    if dv > 0:
        counter2 = counter2 + 6
    templist1 = []
    templist2 = []
    countlist = []
    dv = 0
    for j in player1list[i]:
        templist1.append(j[0])
    for j in player1list:
        templist2.append(j[0])
    if counter1 > counter2 or counter2 > counter1:
        scorelist1.append(counter1)
        scorelist2.append(counter2)
        continue
    elif counter2 == counter1 and counter2 != 0 and counter1 != 0:
        if maxsort(pokersort(templist1), pokersort(templist2)) == True:
            counter1 += 1
            scorelist1.append(counter1)
            scorelist2.append(counter2)
            continue
        elif maxsort(pokersort(templist1), pokersort(templist2)) == False:
            counter2 += 1
            scorelist1.append(counter1)
            scorelist2.append(counter2)
            continue
    templist1 = []
    templist2 = []
    countlist = []
    dv = 0
    for j in player1list[i]:
        templist1.append(j[0])
    sortedddlist = pokersort(templist1)
    for j in range(len(sortedddlist)):
        if sortedddlist[0] + j == sortedddlist[j]:
            dv += 1
            continue
        elif sortedddlist[0] + j != sortedddlist[j]:
            continue
    if dv == 5:
        counter1 = counter1 + 5 + float(sorteddlist[0]/10)
    templist1 = []
    templist2 = []
    countlist = []
    dv = 0
    for j in player2list[i]:
        templist1.append(j[0])
    sortedddlist = pokersort(templist1)
    for j in range(len(sortedddlist)):
        if sortedddlist[0] + j == sortedddlist[j]:
            dv += 1
            continue
        elif sortedddlist[0] + j != sortedddlist[j]:
            continue
    if dv == 5:
        counter2 = counter2 + 5 + float(sorteddlist[0] / 10)
    templist1 = []
    templist2 = []
    countlist = []
    dv = 0
    for j in player1list[i]:
        templist1.append(j[0])
    for j in player2list[i]:
        templist2.append(j[0])
    if counter1 > counter2 or counter2 > counter1:
        scorelist1.append(counter1)
        scorelist2.append(counter2)
        continue
    elif counter2 == counter1 and counter2 != 0 and counter1 != 0:
        if maxsort(pokersort(templist1), pokersort(templist2)) == True:
            counter1 += 1
            scorelist1.append(counter1)
            scorelist2.append(counter2)
            continue
        elif maxsort(pokersort(templist1), pokersort(templist2)) == False:
            counter2 += 1
            scorelist1.append(counter1)
            scorelist2.append(counter2)
            continue
    templist1 = []
    templist2 = []
    countlist = []
    dv = 0
    for j in player1list[i]:
        templist1.append(j[0])
    for j in templist1:
        countr1 = 0
        for k in templist1:
            if k == j:
                countr1 += 1
        countlist.append(countr1)
    if 3 in countlist:
        for k in range(len(countlist)):
            if countlist[k] == 3:
                for j in range(len(scoringlist)):
                    if templist1[k] == scoringlist[j]:
                        counter1 = counter1 + 4 + float(j / 10)
                        break
                    else:
                        continue
    templist1 = []
    templist2 = []
    countlist = []
    dv = 0
    for j in player2list[i]:
        templist1.append(j[0])
    for j in templist1:
        countr1 = 0
        for k in templist1:
            if k == j:
                countr1 += 1
        countlist.append(countr1)
    if 3 in countlist:
        for k in range(len(countlist)):
            if countlist[k] == 3:
                for j in range(len(scoringlist)):
                    if templist1[k] == scoringlist[j]:
                        counter2 = counter2 + 4 + float(j / 10)
                        break
                    else:
                        continue
    templist1 = []
    templist2 = []
    countlist = []
    dv = 0
    for j in player1list[i]:
        templist1.append(j[0])
    for j in player2list[i]:
        templist2.append(j[0])
    if counter1 > counter2 or counter2 > counter1:
        scorelist1.append(counter1)
        scorelist2.append(counter2)
        continue
    elif counter2 == counter1 and counter2 != 0 and counter1 != 0:
        if maxsort(pokersort(templist1), pokersort(templist2)) == True:
            counter1 += 1
            scorelist1.append(counter1)
            scorelist2.append(counter2)
            continue
        elif maxsort(pokersort(templist1), pokersort(templist2)) == False:
            counter2 += 1
            scorelist1.append(counter1)
            scorelist2.append(counter2)
            continue
    templist1 = []
    templist2 = []
    countlist = []
    dv = 0
    for j in player1list[i]:
        templist1.append(j[0])
    for j in templist1:
        countr1 = 0
        for k in templist1:
            if k == j:
                countr1 += 1
        countlist.append(countr1)
    for j in countlist:
        if j == 2:
            dv += 1
        else:
            continue
    if dv == 4:
        for k in range(len(countlist)):
            if countlist[k] == 2:
                for j in range(len(scoringlist)):
                    if templist1[k] == scoringlist[j]:
                        counter1 = counter1 + 3 + float(j / 10)
                        break
                    else:
                        continue
    templist1 = []
    templist2 = []
    countlist = []
    dv = 0
    for j in player2list[i]:
        templist1.append(j[0])
    for j in templist1:
        countr1 = 0
        for k in templist1:
            if k == j:
                countr1 += 1
        countlist.append(countr1)
    for j in countlist:
        if j == 2:
            dv += 1
        else:
            continue
    if dv == 4:
        for k in range(len(countlist)):
            if countlist[k] == 2:
                for j in range(len(scoringlist)):
                    if templist1[k] == scoringlist[j]:
                        counter2 = counter2 + 3 + float(j / 10)
                        break
                    else:
                        continue
    templist1 = []
    templist2 = []
    countlist = []
    dv = 0
    for j in player1list[i]:
        templist1.append(j[0])
    for j in player2list[i]:
        templist2.append(j[0])
    if counter1 > counter2 or counter2 > counter1:
        scorelist1.append(counter1)
        scorelist2.append(counter2)
        continue
    elif counter2 == counter1 and counter2 != 0 and counter1 != 0:
        if maxsort(pokersort(templist1), pokersort(templist2)) == True:
            counter1 += 1
            scorelist1.append(counter1)
            scorelist2.append(counter2)
            continue
        elif maxsort(pokersort(templist1), pokersort(templist2)) == False:
            counter2 += 1
            scorelist1.append(counter1)
            scorelist2.append(counter2)
            continue
    templist1 = []
    templist2 = []
    countlist = []
    dv = 0
    for j in player1list[i]:
        templist1.append(j[0])
    for j in templist1:
        countr1 = 0
        for k in templist1:
            if k == j:
                countr1 += 1
        countlist.append(countr1)
    for j in countlist:
        if j == 2:
            dv += 1
        else:
            continue
    if dv == 2:
        for k in range(len(countlist)):
            if countlist[k] == 2:
                for j in range(len(scoringlist)):
                    if templist1[k] == scoringlist[j]:
                        counter1 = counter1 + 2 + float(j / 10)
                        break
                    else:
                        continue
    templist1 = []
    templist2 = []
    countlist = []
    dv = 0
    for j in player2list[i]:
        templist1.append(j[0])
    for j in templist1:
        countr1 = 0
        for k in templist1:
            if k == j:
                countr1 += 1
        countlist.append(countr1)
    for j in countlist:
        if j == 2:
            dv += 1
        else:
            continue
    if dv == 2:
        for k in range(len(countlist)):
            if countlist[k] == 2:
                for j in range(len(scoringlist)):
                    if templist1[k] == scoringlist[j]:
                        counter2 = counter2 + 2 + float(j / 10)
                        break
                    else:
                        continue
    templist1 = []
    templist2 = []
    countlist = []
    dv = 0
    for j in player1list[i]:
        templist1.append(j[0])
    for j in player2list[i]:
        templist2.append(j[0])
    if counter1 > counter2 or counter2 > counter1:
        scorelist1.append(counter1)
        scorelist2.append(counter2)
        continue
    elif counter2 == counter1 and counter2 != 0 and counter1 != 0:
        if maxsort(pokersort(templist1), pokersort(templist2)) == True:
            counter1 += 1
            scorelist1.append(counter1)
            scorelist2.append(counter2)
            continue
        elif maxsort(pokersort(templist1), pokersort(templist2)) == False:
            counter2 += 1
            scorelist1.append(counter1)
            scorelist2.append(counter2)
            continue
    templist1 = []
    templist2 = []
    countlist = []
    dv = 0
    for j in player1list[i]:
        templist1.append(j[0])
    for j in player2list[i]:
        templist2.append(j[0])
    if maxsort(pokersort(templist1), pokersort(templist2)) == True:
        counter1 += 1
        scorelist1.append(counter1)
        scorelist2.append(counter2)
    elif maxsort(pokersort(templist1), pokersort(templist2)) == False:
        counter2 += 1
        scorelist1.append(counter1)
        scorelist2.append(counter2)

for i in range(1000):
    if scorelist1[i] > scorelist2[i]:
        player1count += 1
    elif scorelist2[i] > scorelist1[i]:
        player2count += 1
print(player1count)

print("this challenge has the same lines of code as it has points")
