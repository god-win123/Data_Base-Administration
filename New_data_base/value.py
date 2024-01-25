import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="my_New_database"
)

mycursor = mydb.cursor()

sql = "INSERT INTO orders (id, name, address) VALUES (%s, %s, %s)"
val = [
    (1, 'John', '15-IV_street'),
    (2,'Peter', '14-lv_street'),
    (3,'Amy', 'Oswal_street'),
    (4,'Hannah','cannon_street'),
    (5,'Michael', 'kolari_street')
]
mycursor.executemany(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")