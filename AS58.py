mport turtle
tom = turtle.Turtle()
def updownfunction(x):
    tom.forward(x)
    tom.left(90)
    tom.forward(75)
    tom.backward(150)
    tom.right(90)
    tom.penup()
    tom.goto(-300,100)
    tom.pendown()

tom.goto(300,0)
tom.goto(-300,0)
tom.speed(0.5)
tom.width(2)
minimum = int(input("whats the minumum?"))
maximum = int(input("whats the maximum"))
q1 = int(input("whats the lower quartile??"))
q3= int(input("whats the upper quartile??"))
q2 = int(input("whats the median???"))
tom.left(90)
tom.penup()
tom.forward(100)
tom.pendown()
tom.right(90)
tom.forward(600)
tom.forward(-600)
updownfunction((0))
updownfunction((q1/maximum)*600)
updownfunction((q3/maximum)*600)
updownfunction((q2/maximum)*600)
updownfunction((maximum/maximum)*600)
interquartile = q3 - q1
tom.penup()
tom.goto(-300+(q1/maximum)*600,175)
tom.pendown()
tom.forward((interquartile/maximum)*600)
tom.penup()
tom.goto(-300+(q1/maximum)*600,25)
tom.pendown()
tom.forward((interquartile/maximum)*600)
turtle.done()
