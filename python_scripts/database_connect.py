#!/usr/bin/python3
"""Connects  to database boli_assurance in localhost server"""
import mysql.connector

mydb = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="root",
    database="boli_assurance"
)
mycursor = mydb.cursor()
