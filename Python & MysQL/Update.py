import mysql.connector

db_name = "new_db"

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "admin",
    database = db_name
)

mycursor = mydb.cursor()

sqlquery = """
            UPDATE Student
            SET Name = "Farhan Nadim"
            WHERE Roll = "0001"
           """

mycursor.execute(sqlquery)

mydb.commit() # when we want to insert or update table for save the data

print("Value Updated Successfully")