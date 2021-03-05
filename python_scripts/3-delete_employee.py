#!/usr/bin/python3
"""Deletes an employee record in the database boli_assurance of SQL"""
import mysql.connector
import sys
from database_connect import mydb, mycursor

sql = ("DELETE FROM employee "
       "WHERE id_employee=%s")
args = sys.argv
val = (int(args[1]),)
mycursor.execute(sql, val)
mydb.commit()
print(mycursor.rowcount, "record deleted.")
mycursor.execute("SELECT * FROM employee")
myresult = mycursor.fetchall()
for x in myresult:
    print(x)
