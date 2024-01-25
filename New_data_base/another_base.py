# import mysql.connector
# mydb = mysql.connector.connect(
#   host="localhost",
#   user="root",
#   password="",
#   database="my_New_database"
# )

# mycursor = mydb.cursor()

# sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
# val = ("John", "Highway 21")
# mycursor.execute(sql, val)

# mydb.commit()

# import mysql.connector
# mydb = mysql.connector.connect(
#     host = 'localhost',
#     user = 'root',
#     password = '',
#     database = 'my_New_database'
# )
# mycursor = mydb.cursor()
# sql = 'INSERT INTO customers(id,name,address) VALUES (%s,%s,%s)'
# val = [
  
#     (2,"Peter", "Lowstreet 4"),
#     (3,'Amy', 'Apple st 652'),
#     (4,'Hannah', 'Mountain 21'),
#     (5,'Michael', 'Valley 345'),
#     (6,'Sandy', 'Ocean blvd 2'),
#     (7,'Betty', 'Green Grass 1'),
#     (8,'Richard', 'Sky st 331'),
#     (9,'Susan', 'One way 98'),
#     (10,'Vicky', 'Yellow Garden 2'),
#     (11,'Ben', 'Park Lane 38'),
#     (12,'William', 'Central st 954'),
#     (13,'Chuck', 'Main Road 989'),
#     (14,'Viola', 'Sideway 1633')
# ]

# mycursor.executemany(sql, val)

# mydb.commit()

# print(mycursor.rowcount, "record inserted.")