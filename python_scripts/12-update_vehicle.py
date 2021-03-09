#!/usr/bin/python3
"""Updates a vehicle record in the database boli_assurance of SQL
at table vehicle"""
import mysql.connector
import sys
from database_connect import mydb, mycursor


def _update(sql, args):
    val = (args[1], args[0])
    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "record updated")
    mycursor.execute("SELECT * FROM vehicle")
    myresult = mycursor.fetchall()
    for x in myresult:
        print(x)


while True:
    print("Which field do you want to update:\n"
          "(1: id_plate, 2: value, 3: date_assurance, 4: time_asssurance, 5: is_assured, 6: id_employee, 7: id_client")
    inp = input()
    if inp == "1":
        print("Enter id and value to update:")
        args = input().split(" ")
        sql = ("UPDATE vehicle "
               "SET id_plate=%s "
               "WHERE id_plate=%s")
        _update(sql, args)
    elif inp == "2":
        print("Enter id and value to update:")
        args = input().split(" ")
        sql = ("UPDATE vehicle "
               "SET value=%s "
               "WHERE id_plate=%s")
        _update(sql, args)
    elif inp == "3":
        print("Enter id and value to update:")
        args = input().split(" ")
        sql = ("UPDATE vehicle "
               "SET date_assurance=%s "
               "WHERE id_plate=%s")
        _update(sql, args)
    elif inp == "4":
        print("Enter id and value to update:")
        args = input().split(" ")
        sql = ("UPDATE vehicle "
               "SET time_asssurance=%s "
               "WHERE id_plate=%s")
        _update(sql, args)
    elif inp== "5":
        print("Enter id and value to update:")
        args = input().split(" ")
        sql = ("UPDATE vehicle "
               "SET is_assured=%s "
               "WHERE id_plate=%s")
        _update(sql, args)
    elif inp== "6":
        print("Enter id and value to update:")
        args = input().split(" ")
        sql = ("UPDATE vehicle "
               "SET id_employee=%s "
               "WHERE id_plate=%s")
        _update(sql, args)
    elif inp== "7":
        print("Enter id and value to update:")
        args = input().split(" ")
        sql = ("UPDATE vehicle "
               "SET id_client=%s "
               "WHERE id_plate=%s")
        _update(sql, args)
    else:
        print("Field doesn't exist.")
    print('---------------------------------------')
