#!/usr/bin/python3
"""Deletes an employee record in the database boli_assurance of SQL"""
import mysql.connector
import sys
from database_connect import mydb, mycursor
from tabulate import tabulate

sql = "SELECT * FROM employee"
mycursor.execute(sql)
myresult = mycursor.fetchall()
for x in myresult:
    print(tabulate(myresult, headers=['id_employee', 'first_name', 'last_name', 'department'], tablefmt='psql'))
