#!/usr/bin/python3
"""Deletes a vehicle record in the database boli_assurance of SQL"""
import mysql.connector
import sys
from database_connect import mydb, mycursor
from tabulate import tabulate

sql = "SELECT * FROM vehicle"
mycursor.execute(sql)
myresult = mycursor.fetchall()
for x in myresult:
    print(tabulate(myresult, headers=['id_plate, value, date_assurance, time_asssurance, is_assured, id_employee, id_client'], tablefmt='psql'))
