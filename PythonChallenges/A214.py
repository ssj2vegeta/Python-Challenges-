#masterdict = {}
#text = input("please enter text")
#for i in text:
    #if i not in masterdict:
        #masterdict[i] = 1
    #else:
        #masterdict[i] += 1
#print(masterdict)
masterdict2 = {}
masterlist = []
mlist2 = []
with open("alice.txt") as file:
    for i in file:
        i = i.strip()
        if len(i) == 0:
            continue
        list1 = i.split()
        masterlist.append(list1)
for i in masterlist:
    for j in i:
        j = j.lower()
        mlist2.append(j)

for i in mlist2:
    for j in i:
        if j not in masterdict2:
            masterdict2[j] = 1
        else:
            masterdict2[j] += 1
print(masterdict2)
maxlen = 0
maxword = ""
for i in mlist2:
    if maxlen < len(i):
        maxlen = len(i)
        maxword = i
    else:
        continue
print(maxword)
