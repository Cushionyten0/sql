import sqlite3

with sqlite3.connect("cars.db") as connection:
    c = connection.cursor()

    orders = (
          ("Ford", "Focus", "2016-05-12"),
          ("Ford", "Focus", "2013-04-11"),
          ("Edge", "Focus", "2015-03-09")
    )
    c.execute("CREATE TABLE orders(make TEXT, model TEXT, order_date DATE)")

    c.executemany("""INSERT INTO orders(make, model, order_date)
    VALUES(?,?,?)""", orders)
    c.execute("""SELECT orders.make, orders.model, inventory.quantity,
    orders.order_date FROM orders, inventory""")

    rows = c.fetchall()

    for r in rows:
        print "Make and Model: " + r[0], r[1]
        print "Quantity: " + str(r[2])
        print "Order Date: " + r[3]
        print " "
