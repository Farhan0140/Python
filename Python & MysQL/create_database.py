import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "admin"
)

db_name = "new_db"

mycursor = mydb.cursor()

sqlquery = "CREATE DATABASE " + db_name

mycursor.execute(sqlquery)