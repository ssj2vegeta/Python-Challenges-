triangularnumberlist = []
for i in range(100):
    triangluarnumber = 0.5 * i * (i+1)
    triangularnumberlist.append(int(triangluarnumber))
print(triangularnumberlist)

with open("wordlist(for triangular number challenge)","r") as file:
    for words in file:
        wordlist = words.split('","')
alphabetlist = [None, 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
totaltriangularnumbers = 0
triangluarnumberwordlist = []
wordlist[0] = "A"
wordlist[-1] = "YOUTH"
print(wordlist)
for i in wordlist:
    print(i)
    count = 0
    for j in i:
        for k in range(len(alphabetlist)):
            if alphabetlist[k] == j:
                count += k
    if count in triangularnumberlist:
        totaltriangularnumbers += 1
        triangluarnumberwordlist.append(i)
    else:
        continue
print(totaltriangularnumbers)
print(triangluarnumberwordlist)
