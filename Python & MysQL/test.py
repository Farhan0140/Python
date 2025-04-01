import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="admin"
) 

# print(mysql.connector.__version__)
print(mydb)
