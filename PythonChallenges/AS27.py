listofallelements = ["hydrogen", "helium", "lithium", "berylium", "boron", "carbon","nitrogen","oxygen", "fluorine", "neon", "sodium", "magnesium"
                      ,"aluminium", "silicon", "phosphurus", "sulfur", "chlorine","argon", "potassium", "scandium", "titanium","vanadium","chromium", "manganese", "iron","cobalt","nickel","zinc"
                     ,"gallium","germanium","arsenic","sermenium", "bromine","krypton", "rubidium","strontium", "yttrium", "zirconium"]
list3 = []
maxlist = []
minlist = []
currentword = ""
for i in listofallelements:
    list2 = []
    currentword = i
    list2.append(currentword)
    for j in listofallelements:
        if currentword[-1] == j[0]:
            currentword = j
            list2.append(currentword)
        else:
            continue
    list3.append(list2)


for i in range(3):
    maxormin_value = 0
    for i in range(0,len(list3)):
        if len(list3[i]) > maxormin_value:
            maxormin_value = len(list3[i])
        else:
            continue
    print(maxormin_value)
    for i in range(0,len(list3)):
        if len(list3[i]) == maxormin_value:
            maxlist.append(list3[i])
            list3.remove(list3[i])
            break
        else:
            continue
    for i in range(0,len(list3)):
        if len(list3[i]) < maxormin_value:
            maxormin_value = len(list3[i])
        else:
            continue
    for i in range(0,len(list3)):
        if len(list3[i]) == maxormin_value:
            minlist.append(list3[i])
            list3.remove(list3[i])
            break
        else:
            continue

print(minlist)
print(maxlist)
