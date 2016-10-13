import sqlite3
import csv

with sqlite3.connect("cars.db") as connection:
    c = connection.cursor()

    cars = {
            ("Focus", "Ford", 1),
            ("Mustang", "Ford", 3),
            ("Edge", "Ford", 4),
            ("CR-V", "Honda", 10),
            ("Accord", "Honda", 3)
    }
    c.execute("CREATE TABLE inventory(name TEXT, brand TEXT, quantity INT)")
    c.executemany("INSERT INTO inventory(name, brand, quantity)\
    VALUES(?,?,?)", cars)
    c.execute("UPDATE inventory SET quantity = 7 WHERE name = 'Focus' ")
    c.execute("SELECT * FROM inventory WHERE brand = 'Ford' ")
    rows = c.fetchall()
    for row in rows:
        print row[0], row[1], row[2]
