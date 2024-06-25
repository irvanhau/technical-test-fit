import mysql.connector as mysql

db = mysql.connect(
    host = "localhost",
    port= 3308,
    user = "root",
    database = "test",
    passwd = "",
)

print(db)