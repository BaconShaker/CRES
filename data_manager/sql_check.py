#!/usr/bin/python
from __init__ import __mike__
import mysql.connector

# Establish connection to SQL server.
db = mysql.connector.connect(**__mike__)
cursor = db.cursor()
print "Logged in as Mike\n"

cursor.execute("SELECT * from Locations")
print cursor.fetchall()