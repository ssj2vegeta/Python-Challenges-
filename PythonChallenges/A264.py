import math
class Planet:
    def __init__(self,name, mass, radius):
        self.mass = mass
        self.radius = radius
        self.planet = name
    def escapevelocity(self):
        ev = math.sqrt((2 * ((6.673 * (10**-11))  * self.mass)) / self.radius)
        print(f"the escape velocity for {self.planet} is: {ev} ms^-2")
