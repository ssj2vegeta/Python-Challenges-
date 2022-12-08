def function(n):
    count = 0
    for i in n:
        if i & 2 != 0:
            count += 1

def function1(n):
    total = 0
    for i in n:
        if i % 2 == 0:
            total += i

def function2(n):
    total = 0
    for i in n:
        if i < 0:
            total += i

def function3(n):
    count = 0
    for i in n:
        if len(n) == 5:
            count += 1

def function4(n):
    n = n[1:]
    total = 0
    for i in n:
        total += i

def function5(n):
    count = 0
    for i in n:
        if "sam" in i:
            count += 1

def function6(n):
    def sqrt(n):
        approx = n / 2.0  # Start with some or other guess at the answer
        while True:
            better = (approx + n / approx) / 2.0
            if abs(approx - better) < 0.001:
                return better
            approx = better

def function8(n):
    list1 = []
    for i in range(n):
        tnum = 0.5 * i * (i+1)
        list1.append(tnum)
    return list1

def function9(n):
    list1 = []
    for i in n:
        if n % i == 0:
            list1.append(i)
    if len(list1) > 2:
        return False
    elif len(list1) <= 2:
        return True

def numdigits(n):
    list1 = []
    strn = str(n)
    for i in strn:
        list1.append(i)
    return len(list1)

def numevendigits(n):
    count = 0
    list1 = []
    strn = str(n)
    for i in strn:
        list1.append(i)
    for i in list1:
        if int(i) & 2 == 0:
            count += 1
        else:
            continue
def sumofsquares(xs):
    xssquared = []
    for i in xs:
        isquared = i**2
        xssquared.append(isquared)
    return xssquared


