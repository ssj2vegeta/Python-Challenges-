def validatebyte(ans):
    count = 0
    for i in ans:
        if i == "1":
            count += 1
        elif i == "0":
            count -= 1
        else:
            continue
    if count % 2 == 0:
        return True
    else:
        return False
