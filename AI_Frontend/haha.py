import mysql.connector

mydb = mysql.connector.connect(
    host       ="127.0.0.1",
    user="root",
    password="Lam2002",
    database="httt"
)
print(mydb)
print(1)