import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="my_New_database"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE orders (id int ,name VARCHAR(255), address VARCHAR(255))")
