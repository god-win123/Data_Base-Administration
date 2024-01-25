import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="my_New_database"
)

mycursor = mydb.cursor()

sql = "INSERT INTO items (id, products) VALUES (%s, %s)"
val = [
    (1,'Car'),
    (2,'Bike'),
    (3,'Plane'),
    (4,'Ship'),
    (5,'Rocket')
]
mycursor.executemany(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")