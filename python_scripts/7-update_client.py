#!/usr/bin/python3
"""Updates a client record in the database boli_assurance of SQL
at table client"""
import mysql.connector
import sys
from database_connect import mydb, mycursor


def _update(sql, args):
    val = (args[1], args[0])
    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "record updated")
    mycursor.execute("SELECT * FROM client")
    myresult = mycursor.fetchall()
    for x in myresult:
        print(x)


while True:
    print("Which field do you want to update:\n"
          "(1: id_client, 2: first_name, 3: last_name, 4: phone, 5: email")
    inp = input()
    if inp == "1":
        print("Enter id and value to update:")
        args = input().split(" ")
        sql = ("UPDATE client "
               "SET id_client=%s "
               "WHERE id_client=%s")
        _update(sql, args)
    elif inp == "2":
        print("Enter id and value to update:")
        args = input().split(" ")
        sql = ("UPDATE client "
               "SET first_name=%s "
               "WHERE id_client=%s")
        _update(sql, args)
    elif inp == "3":
        print("Enter id and value to update:")
        args = input().split(" ")
        sql = ("UPDATE client "
               "SET last_name=%s "
               "WHERE id_client=%s")
        _update(sql, args)
    elif inp == "4":
        print("Enter id and value to update:")
        args = input().split(" ")
        sql = ("UPDATE client "
               "SET phone=%s "
               "WHERE id_client=%s")
        _update(sql, args)
    elif inp== "5":
        print("Enter id and value to update:")
        args = input().split(" ")
        sql = ("UPDATE client "
               "SET phone=%s "
               "WHERE id_client=%s")
        _update(sql, args)
    else:
        print("Field doesn't exist.")
    print('---------------------------------------')
