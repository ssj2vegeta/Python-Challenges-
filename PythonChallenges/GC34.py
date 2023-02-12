def stringmanipulator(word):
    j = list(word)
    reversed_word = ""
    for x in reversed(j):
        reversed_word +=x
    return reversed_word

englishtoromanlist = [ {"0":"","1":"I","2":"II","3":"III","4":"IV","5":"V","6":"VI","7":"VII","8":"VIII", "9": "IX"}, {"0":"","1":"X", "2":"XX","3":"XXX","4":"XL","5":"L","6":"LX","7":"LXX","8":"LXXX","9":"XC"}, {"0":"","1":"C","2":"CC","3":"CCC","4":"CD","5":"D","6":"DC","7":"DCC","8":"DCCC","9":"CM"}, {"0":"","1":"M","2":"MM","3":"MMM"}]
def englishtoroman(number):
    reverse = stringmanipulator(number)
    listed = list(reverse)
    length = len(listed)
    list1 = []
    empt = ""
    f = 0
    for k in englishtoromanlist:
        if f <= (len(listed)-1):
            for j in k:
                if j == listed[f]:
                    f += 1
                    list1.append(k[j])
                    break
                else:
                    continue
        else:
            break
    for i in range(len(list1)-1, -1, -1):
        empt = empt + list1[i]
    return empt

romantoenglishlist1 = {"I":"1","II":"2","III":"3","IV":"4","V":"5","VI":"6","VII":"7","VIII":"8", "IX": "9"}
romantoenglishlist2 = {"X":"1", "XX":"2","XXX":"3","XL":4,"L":"5","LX":"6","LXX":"7","LXXX":"8","XC":"9"}
romantoenglishlist3 = {"C":"1","CC":"2","CCC":"3","CD":"4","D":"5","DC":"6","DCC":"7","DCCC":"8","CM":"9"}
romantoenglishlist4 = {"M":"1","MM":"2","MMM":"3"}


def romantoenglish(number):
    reverse = stringmanipulator(number)
    listed = list(number)
    list1 = []
    list2 = []
    list3 = []
    list4 = []
    finallist = []
    empt = ""
    if "I" or "V" in number:
        templist = []
        for i in romantoenglishlist1:
            if i in number:
                list1.append(i)
        for i in list1:
            templist.append(len(i))
        if len(templist) > 0:
            max1 = max(templist)
            finallist.append(romantoenglishlist1[list1[templist.index(max1)]])
            listed = listed[:(len(listed) - len(list1[(templist.index(max1))]))]
            number = ""
            for i in listed:
                number = number + i
        else:
            finallist.append("0")
    if "X" or "L" in number:
        templist = []
        for i in romantoenglishlist2:
            if i in number:
                list2.append(i)
        for i in list2:
            templist.append(len(i))
        if len(templist) > 0:
            max1 = max(templist)
            finallist.append(romantoenglishlist2[list2[templist.index(max1)]])
        else:
            finallist.append("0")
    if "C" or "D" in number:
        templist = []
        for i in romantoenglishlist3:
            if i in number:
                list3.append(i)
        for i in list3:
            templist.append(len(i))
        if len(templist) > 0:
            max1 = max(templist)
            finallist.append(romantoenglishlist3[list3[templist.index(max1)]])
            listed = listed[:(len(listed) - len(list3[(templist.index(max1))]))]
            number = ""
            for i in listed:
                number = number + i
        else:
            finallist.append("0")

    if "M" in number:
        templist = []
        for i in romantoenglishlist4:
            if i in number:
                list4.append(i)
        for i in list4:
            templist.append(len(i))
        if len(templist) > 0:
            max1 = max(templist)
            finallist.append(romantoenglishlist4[list4[templist.index(max1)]])
            listed = listed[:(len(listed) - len(list4[(templist.index(max1))]))]
            number = ""
            for i in listed:
                number = number + i
            print(number)
        elif len(templist) == 0:
            finallist.append("0")
    for i in range(len(finallist)-1, -1, -1):
        empt = empt  + finallist[i]
    return empt
for i in range(101):
    print(englishtoroman(str(i)))
