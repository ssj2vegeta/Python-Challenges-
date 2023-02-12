import turtle
turtle.speed(15)

class pattern():
    def __init__(self, angle: int, times: int):
        self.__angle = angle # Integer
        self.__times = times # Integer

    def draw_pattern(self):
        turtle.setheading(0)
        turtle.penup()
        turtle.goto(0,0)
        turtle.pendown()
        colors = ['red', 'purple', 'blue', 'green', 'orange', 'yellow']
        turtle.setup(800, 600)  # setting window dimensions
        turtle.bgcolor('black')
        for x in range(self.__times):
            turtle.pencolor(colors[x % 6])
            turtle.width(x / 100 + 1)
            turtle.forward(x)
            turtle.left(self.__angle)
lst = []
with open("angles.txt","r") as file:
    for j in file:
        lst.append(j)
for i in range(0,10,2):
        mypattern = pattern(int(lst[i]), int(lst[i+1]))  # Demo pattern
        mypattern.draw_pattern()
turtle.done()
