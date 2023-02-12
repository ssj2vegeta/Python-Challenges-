import csv
firstname = []
lastname = []
with open("employees.txt","r") as file:
    reader = csv.reader(file)
    for i in reader:
        firstname.append(i[0])
        lastname.append(i[1])

class Employee:
    def __init__(self, FirstName: str, LastName: str):
        self.FirstName = FirstName.lower()
        self.LastName = LastName.lower()
        self.FullName = self.FirstName + "." + self.LastName
        self.Email = self.FullName + "@company.com"

    def PrintDetails(self):
        print(self.FirstName, self.LastName, self.Email)

for i in range(len(firstname)):
    employee = Employee(firstname[i], lastname[i])
    employee.PrintDetails()
