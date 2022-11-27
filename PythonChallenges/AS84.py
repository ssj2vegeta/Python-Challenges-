mport string
import random
alphabet = list(string.ascii_lowercase)
caesarshiftedalphabet = list(string.ascii_lowercase)

caesarshiftedalphabet.remove('a')
caesarshiftedalphabet.append('a')

msgtodecrypt = input("please enter your message")
msgtodecrypt = msgtodecrypt.lower().strip()
decryptpedmsg = ""
for i in msgtodecrypt:
    for j in range(len(caesarshiftedalphabet)):
        if caesarshiftedalphabet[j] == i:
            decryptpedmsg = decryptpedmsg + alphabet[j]
        else:
            continue
list3 = []
with open("listofallwords", "r") as new_file:
    for i in new_file:
        list3.append(i.rstrip())
list2 = []
for i in list3:
    if len(decryptpedmsg) == len(i):
        if decryptpedmsg[0] == i[0] and decryptpedmsg[len(decryptpedmsg)-1] == i[len(i)-1]:
            list2.append(i)
            break
        else:
            continue
    else:
        continue
if len(list2) == 0:
    print("unable to decipher")
elif len(list2) == 1:
    print(list2[0])
