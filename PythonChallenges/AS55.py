import turtle
seed = int(input("please enter your seed)"))#doesnt work with negative numbers
x = (seed/2)**0.5
y = x
def main():
    star(0,0)
    star(x,y)
    star(x,-y)
    star(-x,-y)
    star(-x,y)


def star(x=0, y=0):
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    turtle.setheading(0)
    turtle.left(144)
    for i in range(5):
        turtle.forward(100)
        turtle.right(144)

if __name__ == "__main__":
    main()
