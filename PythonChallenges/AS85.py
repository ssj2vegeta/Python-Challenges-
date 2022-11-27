list1 = []
with open("if.txt","r") as whole_file:
    for i in whole_file:
        list1.append(i.strip())
        print(i)
list2 = []
for i in list1:
    if "if" or "If" in i:
        list2.append("if")
with open("if.txt","a") as whole_file:
    line_to_write = "the number of ifs is" + str(len(list2))
    whole_file.write(line_to_write)
list3 = []
with open("mam.txt","r") as whole_file:
    for i in whole_file:
        list3.append(i.strip())
        print(i)
list4 = []
for i in list3:
    if "if" or "If" in i:
        list4.append("if")
with open("mam.txt","a") as whole_file:
    line_to_write = "the number of ifs is" + str(len(list4))
    whole_file.write(line_to_write)

if len(list2) > len(list4):
    print(f"if.txt has  more ifs: {len(list2)}")
if len(list4) > len(list2):
    print(f"mam.txt has  more ifs: {len(list4)}")
