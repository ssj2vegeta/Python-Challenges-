list = ["banana", "apple"]
list.sort()
print(list)


f = open("sorted.txt", "a")
f.write(str(list))
f.close()

#open and read the file after the appending:
f = open("sorted.txt", "r")
print(f.read())
