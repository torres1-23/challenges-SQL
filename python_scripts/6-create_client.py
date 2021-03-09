#!/usr/bin/python3
""" Creates a client record in the database boli_assurance of SQL"""
import mysql.connector
import sys
from database_connect import mydb, mycursor

sql = ("INSERT INTO client (id_client, first_name, last_name, phone, email) VALUES (%s, %s, %s, %s, %s)")
args = sys.argv
val = (int(args[1]), args[2], args[3], int(args[4]), args[5])
mycursor.execute(sql, val)
mydb.commit()
print(mycursor.rowcount, "record inserted")
mycursor.execute("SELECT * FROM client")
myresult = mycursor.fetchall()
for x in myresult:
    print(x)
