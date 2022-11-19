list1 = [".", " ", ",", "?"]
list2 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', "A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
list3 = ['0','1','2','3','4','5','6','7','8','9']
emptlist = []
def main():
    password = input("Please input a password (must have 2 letters at start, minimum of 8 and maximum of 14 letters, no periods, spaces or punctuation marks, numbers cant be used in the middle of the plate and first number cant be 0):")
    if is_valid(password):
        print("Valid")
    else:
        print("Invalid")

def lenfunction(s):
    if len(s) >= 8 and len(s) <= 14:
        return True
    else:
        return False

def numberchecker(s):
    f = 0
    d = list(s)
    x = len(d)
    for i in range(0,x-1):
        if d[i] in list2:
            continue
        elif d[i] in list3:

                if d[i+1] in list2:
                    f += 1
                else:
                    continue
    if f == 0:
        return True
    else:
        return False



def allowedletters(s):
    f = 0
    for i in s:
        if i in list1:
            f += 1
        else:
            continue
    if f == 0:
        return True
    else:
        return False

def startingletters(s):
    splits = s[0:2]
    f = 0
    for i in splits:
        if i in list2:
            f = f + 1
        else:
            continue
    if f == 2:
        return True
    else:
        return False
def zerochecker(s):


    z = 0
    f = 0
    for i in s:
        if f > 0 and z == 0:
            break
        elif z > 0 and f == 0:
            break


        if i in list2:
            continue
        elif i in list3:
            if i == list3[0]:
                f += 1
            else:
                z += 1
        if f > 0 and z == 0:
            return False
        elif z > 0 and f == 0:
            return True





def is_valid(s):
    if lenfunction(s) == True and numberchecker(s) == True and allowedletters(s) == True and startingletters(s) == True and zerochecker(s) == True:
        return True
    else:
        return False





main()
