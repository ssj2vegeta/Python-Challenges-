import sqlite3
import random
conn = sqlite3.connect('Fastcars.sqlite')
def create_top50_db():
    with conn:
        conn.execute("CREATE TABLE cars(id INTEGER PRIMARY KEY, Name TEXT, TopSpeed INT")
        conn.execute("INSERT INTO Cars(Name,TopSpeed) VALUES('Porsche 911, Carrera 4s', 185")
        conn.execute("INSERT INTO Cars(Name,TopSpeed) VALUES('Audi R8', 187")


def print_all_cars():
    with conn:
        cur = conn.execute("SELECT id, Name, TopSpeed from Cars")
    for row in cur:
        print("ID ", row[0])
        print("Name: ", row[1])
        print("Top Speed: ", row[2], "mph\n")
    print("The End")


def print_one_row():
    with conn:
        PrintCar = input("Car ID:")
create_top50_db()
print_all_cars()
