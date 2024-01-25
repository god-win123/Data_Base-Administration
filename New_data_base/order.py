import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="my_New_database"
)

mycursor = mydb.cursor()

sql = "SELECT * FROM customers ORDER BY name DESC "

mycursor.execute(sql)

myresult = mycursor.fetchall()

for x in myresult:
  print(x)