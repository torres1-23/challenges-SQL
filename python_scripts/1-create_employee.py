#!/usr/bin/python3
""" Creates an employee record in the database boli_assurance of SQL"""
import mysql.connector
import sys
from database_connect import mydb, mycursor

sql = ("INSERT INTO employee (id_employee, first_name, last_name, department) "
       "VALUES (%s, %s, %s, %s)")
args = sys.argv
val = (int(args[1]), args[2], args[3], args[4])
mycursor.execute(sql, val)
mydb.commit()
print(mycursor.rowcount, "record inserted.")
mycursor.execute("SELECT * FROM employee")
myresult = mycursor.fetchall()
for x in myresult:
    print(x)
