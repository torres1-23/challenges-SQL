#!/usr/bin/python3
""" Creates a vehicle record in the database boli_assurance of SQL"""
import mysql.connector
import sys
from database_connect import mydb, mycursor

sql = ("INSERT INTO vehicle (id_plate, value, date_assurance, time_asssurance, is_assured, id_employee, id_client) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)")
args = sys.argv
val = (int(args[1]), int(args[2]), args[3], int(args[4]), (args[5]), int(args[6]), int(args[7]))
mycursor.execute(sql, val)
mydb.commit()
print(mycursor.rowcount, "record inserted")
mycursor.execute("SELECT * FROM vehicle")
myresult = mycursor.fetchall()
for x in myresult:
    print(x)
