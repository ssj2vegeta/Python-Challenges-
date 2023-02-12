import math



class Point:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    # exercise 2
    def reflect(self):
        return self.x, self.y*-1
    # exercise 3
    def slopefromorigin(self):
        gradient = self.y/self.x
        return gradient

    def returnn(self):
        return self.x, self.y

class Rectangle:

    def __init__(self, posn, w, h):
        self.corner = posn
        self.width = w
        self.height = h

    def __str__(self):
        return  "({0}, {1}, {2})".format(self.corner, self.width, self.height)
    def area(self):
        return self.width * self.height
    def perimeter(self):
        return 2*self.width + 2*self.height
    def inverter(self):
        return self.width, self.height == self.height, self.width
    def contains(self, point):
        if (point.x > self.corner.x - self.width/2 and point.x < self.corner.x + self.width/2) and (point.y > self.corner.y - self.height/2 and point.y < self.corner.y + self.height/2):
            return True
        else:
            return False
    def collision(self, point, width, height):
        self.casetopright = (self.corner.x + self.width/2, self.corner.y + self.height/2)
        self.casetopleft = (self.corner.x - self.width / 2, self.corner.y + self.height / 2)
        self.casebottomright = (self.corner.x + self.width/2, self.corner.y - self.height/2)
        self.casebottomleft = (self.corner.x + self.width / 2, self.corner.y - self.height / 2)
        casetopright = (point.x + width/2, point.y + height/2)
        casetopleft = (point.x - width / 2, point.y + height / 2)
        casebottomright = (point.x + width / 2, point.y - height / 2)
        casebottomleft = (point.x - width / 2, point.y - height / 2)
        if (self.casetopright[1] > casebottomleft[1] and self.casetopleft[1] > casebottomleft[1]) and (casebottomleft[0] < self.casetopright[0] and casebottomleft[0] > self.casetopleft[0]):
            return True
        elif (self.casetopright[1] > casebottomright[1] and self.casetopleft[1] > casebottomright[1]) and (casebottomright[0] < self.casetopright[0] and casebottom[0] > self.casetopleft[0]):
            return True
        elif (self.casebottomright[1] < casetopleft[1]) and (casetopleft[0] < self.casetbottomright[0] and casetop[0] > self.casebottomleft[0]):
            return True
        elif (self.casebottomleft[1] < casetopright[1]) and (casetopright[0] < self.casetopright[0] and casetopright[0] > self.casetopleft[0]):
            return True
        else:
            return False 




p = Rectangle(Point(5,6), 5, 5)

