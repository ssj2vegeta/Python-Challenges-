def polygon(sides,length,repetitions = 4):
    for i in range(repetitions):
        for i in range(sides):
            tom.forward(length)
            tom.right(360 / sides)
        if sides % 2 != 0:
            for i in range(round(sides/2)):
                tom.forward(length)
                tom.right(360 / sides)
            tom.setheading(90)
            continue
        if sides % 2 == 0:
            for i in range(int(sides/2)):
                tom.forward(length)
                tom.right(360 / sides)
            tom.setheading(90)
            continue
sides = int(input("how many sides do you want?"))
length = int(input("how long do you want your sides to be?"))
polygon(sides, length)
