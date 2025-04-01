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
            INSERT INTO student(Roll, Name, Email, Phone)
            VALUES
                ('0001', 'Daniel', 'dujusrag@tobfuze.hk', '514422879'),
                ('0002', 'Sue', 'rotdup@pizicauv.tg', '356024605'),
                ('0003', 'Rosa', 'uhizeb@de.cn', '923672973'),
                ('0004', 'Henry', 'ahunupduh@binono.va', '627786573'),
                ('0005', 'Martin', 'on@sirrel.ga', '209927372')
           """

mycursor.execute(sqlquery)

mydb.commit() # when we want to insert or update table for save the data

print("Value Inserted Successfully")