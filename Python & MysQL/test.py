import mysql.connector
# print(mysql.connector.__version__)

mydb_connection = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="admin"
) 
print(mydb_connection)

