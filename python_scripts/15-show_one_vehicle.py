#!/usr/bin/python3
"""show a vehicle record in the database boli_assurance of SQL"""
import mysql.connector
import sys
from database_connect import mydb, mycursor
from tabulate import tabulate

sql = ("SELECT * FROM vehicle WHERE id_plate=%s")
args = sys.argv
val = (int(args[1]), )
mycursor.execute(sql, val)
myresult = mycursor.fetchall()
for x in myresult:
    print(tabulate(myresult, headers=['id_plate, value, date_assurance, time_asssurance, is_assured, id_employee, id_client'], tablefmt='psql'))
