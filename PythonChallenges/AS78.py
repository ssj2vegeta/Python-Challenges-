import turtle

# turtle object
pen = turtle.Turtle()

# function for creation of eye
def eye(col, rad):
    pen.down()
    pen.fillcolor(col)
    pen.begin_fill()
    pen.circle(rad)
    pen.end_fill()
    pen.up()


# draw face
pen.fillcolor('yellow')
pen.begin_fill()
pen.circle(100)
pen.end_fill()
pen.up()

import turtle

smiles = turtle.Turtle()

smiles.penup()
smiles.goto(-105,155)
smiles.pendown()
smiles.goto(-45,115)

smiles.penup()
smiles.goto(-75,75)
smiles.pendown()
smiles.circle(10)

smiles.penup()
smiles.goto(105,155)
smiles.pendown()
smiles.goto(45,115)

smiles.penup()
smiles.goto(75,75)
smiles.pendown()
smiles.circle(10)

smiles.penup()
smiles.goto(0,25)
smiles.pendown()
smiles.circle(-100,80)

smiles.penup()
smiles.setheading(180)
smiles.goto(0,25)
smiles.pendown()
smiles.circle(100,80)

turtle.done()

import turtle as t 
t.speed(5)

#face
t.goto(0,0)
t.circle(80)

#left eye
t.penup()
t.goto(-40,100)
t.pendown()

t.color("darkgreen")
t.begin_fill()
t.circle(10)
t.end_fill()

#right eye
t.penup()
t.goto(40,100)
t.pendown()

t.color("darkgreen")
t.begin_fill()
t.circle(10)
t.end_fill()

#nose
t.penup()
t.goto(0,100)
t.pendown()

t.color("black")
t.right(90)
t.forward(40)


#mouth
t.penup()
t.goto(-30,30)
t.pendown()

t.color("red")
t.left(90)
t.forward(60)

t. hideturtle()

# draw eyes
pen.goto(-40, 120)
eye('white', 15)
pen.goto(-37, 125)
eye('black', 5)
pen.goto(40, 120)
eye('white', 15)
pen.goto(40, 125)
eye('black', 5)

# draw nose
pen.goto(0, 75)
eye('black', 8)

# draw mouth
pen.goto(-40, 85)
pen.down()
pen.right(90)
pen.circle(40, 180)
pen.up()

# draw tongue
pen.goto(-10, 45)
pen.down()
pen.right(180)
pen.fillcolor('red')
pen.begin_fill()
pen.circle(10, 180)
pen.end_fill()
pen.hideturtle()
