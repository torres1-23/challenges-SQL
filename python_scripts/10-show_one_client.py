#!/usr/bin/python3
"""Deletes a client record in the database boli_assurance of SQL"""
import mysql.connector
import sys
from database_connect import mydb, mycursor
from tabulate import tabulate

sql = ("SELECT * FROM client WHERE id_client=%s")
args = sys.argv
val = (int(args[1]), )
mycursor.execute(sql, val)
myresult = mycursor.fetchall()
for x in myresult:
    print(tabulate(myresult, headers=['id_client', 'first_name', 'last_name', 'phone', 'email'], tablefmt='psql'))
