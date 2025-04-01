import mysql.connector

db_name = "new_db"

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "admin",
    database = db_name
)

table_name = "Student"

mycursor = mydb.cursor()

sqlquery = """
            CREATE TABLE Student(
                Roll CHAR(4) PRIMARY KEY,
                Name VARCHAR(100),
                Email VARCHAR(100) UNIQUE,
                Phone VARCHAR(100) UNIQUE
            )
           """

mycursor.execute(sqlquery)