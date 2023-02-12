import turtle
import random
for i in range(10):
    j = random.randint(0, 360)
    turtle.forward(100)
    turtle.right(j)
turtle.done()
