#!/usr/bin/python3
import mysql.connector
import sys


mydb = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="root",
    database="boli_assurance"
)
mycursor = mydb.cursor()
sql = ("INSERT INTO employee (id_employee, first_name, last_name, department) "
       "VALUES (%s, %s, %s, %s)")
args = sys.argv
val = (int(args[1]), args[2], args[3], args[4])
print(val)
mycursor.execute(sql, val)
mydb.commit()
print(mycursor.rowcount, "record inserted.")
mycursor.execute("SELECT * FROM employee")
myresult = mycursor.fetchall()
for x in myresult:
    print(x)
