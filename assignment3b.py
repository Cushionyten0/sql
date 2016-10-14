import sqlite3

with sqlite3.connect("newnum.db") as connection:
    c = connection.cursor()

    sql = {"AVG": "SELECT avg(integer) from integers",
           "MAX": "SELECT max(integer) from integers",
           "MIN": "SELECT min(integer) from integers",
           "SUM": "SELECT sum(integer) from integers"}

    while True:
        user_input = raw_input("What opperation would you like to do: ")
        if user_input == "EXIT":
            break
        # can also write it as c.execute("SELECT {}(integer)".format(dict))
        c.execute(sql.get(user_input))
        this = c.fetchone()
        print(this[0])
