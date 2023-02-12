import sqlite3
import random
conn = sqlite3.connect('Fastcars.sqlite')
def create_top50_db():
    with conn:
        conn.execute("CREATE TABLE cars(id INTEGER PRIMARY KEY, Name TEXT, TopSpeed INT")
        conn.execute("INSERT INTO Cars(Name,TopSpeed) VALUES('Porsche 911, Carrera 4s', 185")
        conn.execute("INSERT INTO Cars(Name,TopSpeed) VALUES('Audi R8', 187")
