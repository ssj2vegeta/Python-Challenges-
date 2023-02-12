import math



class Point:
    """ Create a new Point, at coordinates x, y """

    def __init__(self, x=0, y=0):
        """ Create a new point at x, y """
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
def distance(p1, p2):
    return math.sqrt( (p1.x-p2.x)**2 + (p1.y-p2.y)**2 )

P = Point(5,4)
K = Point(2,3)
print(K.slopefromorigin())

# exercise 6

class SMS_store():
    def __init__(self, has_been_viewed, from_number, time_arrived, text_of_SMS):
        self.n = has_been_viewed
        self.k = from_number
        self.t = time_arrived
        self.tos = text_of_SMS
        self.count = 0
    def add_new_arrival(self, from_number, time_arrived, text_of_SMS):
        tuple = (from_number, time_arrived, text_of_SMS)
        self.n = False
        self.count += 1
        return Tuple
    def message_count():
        return self.count
    def get_message(self):
        ...

my_inbox.delete(i)
my_inbox.clear() 
