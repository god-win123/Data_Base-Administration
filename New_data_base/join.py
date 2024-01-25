import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="my_New_database"
)

mycursor = mydb.cursor()

sql = "SELECT \
  orders.name AS order, \
  items.name AS favoratie \
  FROM orders \
  INNER JOIN products ON orders.address = items.id"

mycursor.execute(sql)

myresult = mycursor.fetchall()

for x in myresult:
  print(x)