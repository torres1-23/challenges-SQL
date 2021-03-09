#!/usr/bin/python3
"""Deletes a client record in the database boli_assurance of SQL"""
import mysql.connector
import sys
from database_connect import mydb, mycursor

sql = ("DELETE FROM client "
       "WHERE id_client=%s")
args = sys.argv
val = (int(args[1]),)
mycursor.execute(sql, val)
mydb.commit()
print(mycursor.rowcount, "record deleted")
mycursor.execute("SELECT * FROM client")
myresult = mycursor.fetchall()
for x in myresult:
    print(x)
