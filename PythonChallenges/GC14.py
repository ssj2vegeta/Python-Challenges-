multiply = int(input("which time table would you like?"))
for i in range(multiply):
    for j in range(multiply + 1):
        print(f"{multiply} x {j} == {multiply*j}")
    break
