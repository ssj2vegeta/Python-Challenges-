def binarysearch(list1, item):
    minindex = 0
    maxindex = len(list1) - 1
    while minindex <= maxindex:
        midpoint = minindex + (maxindex-minindex) // 2
        midvalue = list1[midpoint]
        if midvalue > item:
            maxindex = midpoint - 1
        elif midvalue < item:
            minindex = midpoint + 1
        else:
            return midvalue
    return "Item not found"
