import sqlite3
from random import randint

with sqlite3.connect("newnum.db") as connection:
    c = connection.cursor()
    random_list = []

    for x in range(100):
        random_list.append(randint(1, 100000))
    random_list = [(i,) for i in random_list]

    c.execute("DROP TABLE IF EXISTS integers")
    c.execute("CREATE TABLE integers(integer INT)")
    c.executemany("INSERT INTO integers VALUES(?)", random_list)

    c.execute("SELECT * FROM integers")
    ints = c.fetchall()

    for i in ints:
        print[i[0]]
