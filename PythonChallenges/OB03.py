class WrexhamFC:
    def __init__(self, PlayerNumber : str, Forename : str, Surname : str, Position : str, CommunityInvolvement = 0, Injured = False):
        self.playernumber = PlayerNumber
        self.Forename = Forename
        self.Surname = Surname
        self.Position = Position
        self.CommunityInvolvement = CommunityInvolvement
        self.Injured = Injured

    def getplayerinfo(self):
        return self.Forename, self.Surname, self.Position

    def changecommunityobject(self, change):
        self.CommunityInvolvement = change
        return self.CommunityInvolvement
    def ChangeInjured(self):
        return self.Injured

number = []
forename = []
surname = []
position = []
ci = []
with open("wrexham.txt","r")as file:
    count = 0
    for i in file:
        if count == 0:
            number.append(i.strip())
            count += 1
            continue
        elif count == 1:
            forename.append(i.strip())
            count += 1
            continue
        elif count == 2:
            surname.append(i.strip())
            count += 1
            continue
        elif count == 3:
            position.append(i.strip())
            count += 1
            continue
        elif count == 4:
            ci.append(i.strip())
            count += 1
            continue
        elif count == 5:
            count = 0
            continue

for i in range(len(ci)):
    wrexham = WrexhamFC(number[i], forename[i], surname[i], position[i])
    print(wrexham.getplayerinfo())
    print(f"community involvements: {wrexham.changecommunityobject(ci[i])}")
    print(f"currently injured: {wrexham.ChangeInjured()}")
