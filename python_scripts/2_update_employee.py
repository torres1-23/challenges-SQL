#!/usr/bin/python3
"""Updates an employee record in the database boli_assurance of SQL
at table employee"""
import mysql.connector
import sys
from database_connect import mydb, mycursor


def _update(sql, args):
    val = (args[1], args[0])
    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "record updated")
    mycursor.execute("SELECT * FROM employee")
    myresult = mycursor.fetchall()
    for x in myresult:
        print(x)


while True:
    print("Which field do you want to update:\n"
          "(1: id_employee, 2: first_name, 3: last_name, 4: department")
    inp = input()
    if inp == "1":
        print("Enter id and value to update:")
        args = input().split(" ")
        sql = ("UPDATE employee "
               "SET id_employee=%s "
               "WHERE id_employee=%s")
        _update(sql, args)
    elif inp == "2":
        print("Enter id and value to update:")
        args = input().split(" ")
        sql = ("UPDATE employee "
               "SET first_name=%s "
               "WHERE id_employee=%s")
        _update(sql, args)
    elif inp == "3":
        print("Enter id and value to update:")
        args = input().split(" ")
        sql = ("UPDATE employee "
               "SET last_name=%s "
               "WHERE id_employee=%s")
        _update(sql, args)
    elif inp == "4":
        print("Enter id and value to update:")
        args = input().split(" ")
        sql = ("UPDATE employee "
               "SET department=%s "
               "WHERE id_employee=%s")
        _update(sql, args)
    else:
        print("Field doesn't exist.")
    print('---------------------------------------')
