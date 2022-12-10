list1 = []
list2 = []
list3 = []
list4 = []
password = input("input some text please")
for i in password:
    list1.append(i)
    list2.append(i)

for i in list1:
    if i in list3:
        continue
    count = 0
    for j in list2:
        if j == i:
            count+= 1
    if count > 0:
        list3.append(i)
        list4.append(count)

print(list1)
print(list2)
print(list3)
print(list4)
maxlist = []
minlist = []
for i in range(3):
    maxormin_value = 0
    for i in range(0,len(list4)):
        if list4[i] > maxormin_value:
            maxormin_value = list4[i]
        else:
            continue
    for i in range(0,len(list4)):
        if list4[i] == maxormin_value:
            maxlist.append(list3[i])
            list3.remove(list3[i])
            list4.remove(list4[i])
            break
        else:
            continue
    for i in range(0,len(list4)):
        if len(list3[i]) < maxormin_value:
            maxormin_value = list4[i]
        else:
            continue
    for i in range(0,len(list4)):
        if list4[i] == maxormin_value:
            minlist.append(list3[i])
            list3.remove(list3[i])
            list4.remove(list4[i])
            break
        else:
            continue

print(minlist)
print(maxlist)
