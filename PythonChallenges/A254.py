class CarRecord():
    def __init__(self, VehicleID, Registration, DateofRegistration, EngineSize, PurchasePrice):
        self.a = VehicleID
        self.b = Registration
        self.c = DateofRegistration
        self.d = EngineSize
        self.e = PurchasePrice
    def array(self):
        return [self.a, self.b, self.c, self.d, self.e]

list1 = []
input1 = int(input("how many cars?"))
for i in range(input1):
    id = input("id please")
    registration = input("registration?")
    dateofregistration = input("date of registration?")
    enginesize = input("engine size?")
    purchaseprice = input("purchase price?")
    k = CarRecord(id, registration, dateofregistration, enginesize, purchaseprice)
    list1.append(k.array())

print(list1)
