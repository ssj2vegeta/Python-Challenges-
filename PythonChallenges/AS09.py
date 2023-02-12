import random
listofwords = []
with open("wordlist(for triangular number challenge)", "r") as file:
    for i in file:
        i = i.lower()
        splitlist = i.split(",")
        for k in splitlist:
            k = k.strip()
            k = k[1:len(k)-1]
            listofwords.append(k)
listofallsymbols = []
symbols = "#$%&'()*+,-./:;<=>?@[\]^_`{|}~"
for i in symbols :
    listofallsymbols.append(i)
masterstring = ""
word = random.choice(listofwords)
print(word)
selectedlist = []
selectedlist2 = []
count = 0
while count < 10:
    randomword = random.choice(listofwords)
    if len(randomword) == len(word):
        selectedlist.append(randomword)
        count += 1
    else:
        continue
selectedlist.append(word)
print(selectedlist)
print(selectedlist2)
wordsinstring = random.randint(5,10)
wordcount = 0
masterstring = masterstring + random.choice(listofallsymbols)
while wordcount < wordsinstring:
    k = random.randint(1,7)
    if k == 7 and masterstring[len(masterstring)-1] in listofallsymbols:
        randomrandom = random.choice(selectedlist)
        masterstring = masterstring + randomrandom
        selectedlist2.append(randomrandom)
        selectedlist.remove(randomrandom)
        wordcount += 1
        if wordcount == wordsinstring - 1 and word not in masterstring:
            masterstring = masterstring + random.choice(listofallsymbols)
            masterstring = masterstring + word
            wordcount += 1
    elif k != 7 or masterstring[len(masterstring)-1] not in listofallsymbols:
        randomsymbol = random.choice(listofallsymbols)
        if randomsymbol == "[":
            masterstring = masterstring + randomsymbol
            o = random.randint(3,7)
            count = 0
            while count < o:
                rand = random.choice(listofallsymbols)
                if rand == "[":
                    continue
                else:
                    masterstring = masterstring + rand
                    count += 1
            masterstring = masterstring + "]"
        else:
            masterstring = masterstring + randomsymbol
            continue
attempts = 5
while attempts > 0:
    print(masterstring)
    print("attempts remaining: ",end ="")
    for i in range(attempts):
        print("*",end="")
    print()
    guess = input("what is your guess")
    if guess == word:
        print("You have successfully hacked this terminal!")
        break
    elif guess != word and guess in selectedlist2:
        likeness = 0
        list1 = list(word)
        list2 = list(guess)
        for i in range(len(list1)):
            if list1[i] == list2[i]:
                likeness += 1
            else:
                continue
        attempts -= 1
        print(f"Likeness: {likeness}")
        continue
    elif guess[0] == "[" and guess[len(guess) -1] == "]" and guess in masterstring:
        attempts += 1
        masterstring = masterstring.replace(guess, "")
    else:
        attempts -= 1
if attempts == 0:
    print("unsuccessful")
