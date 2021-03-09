#!/usr/bin/python3
"""Deletes an employee record in the database boli_assurance of SQL"""
import mysql.connector
import sys
from database_connect import mydb, mycursor
from tabulate import tabulate

sql = ("SELECT * FROM employee "
       "WHERE id_employee=%s")
args = sys.argv
val = (int(args[1]), )
mycursor.execute(sql, val)
myresult = mycursor.fetchall()
for x in myresult:
    print(tabulate(myresult, headers=['id_employee', 'first_name', 'last_name', 'department'], tablefmt='psql'))
