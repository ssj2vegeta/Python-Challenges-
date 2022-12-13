emptlist = [0,1]

for i in range(100):
    emptlist.append(emptlist[len(emptlist)-1]+emptlist[len(emptlist)-2])
    print(emptlist)
print(emptlist)
