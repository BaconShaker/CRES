#!/Users/AsianCheddar/the_matrix/bin/python

# --------------------  --------------------------
# Example of user_imputs
	# Height (DEPARTURE):   21
	# Pickup Score          34.38
	# Collectable Material  19.84
	# Height (ARRIVAL):     32
	# Duration:             0
	# Service Fee           0.15
	# Gallons on Departure  122.18
	# Notes:                0
	# Donation Rate         0.06
	# Miles in Route        7.5
	# Stops on Route        1
	# Total Distance        7.5
	# Date                  2015-04-17 16:41:52.958848
	# Fuel Surcharge        2.465625
	# Gallons on Arrival    186.18
	# Number of Stops       1
	# Contact Person        Robby Shintani
	# Expected Revenue      4.17
	# Diesel Price          2.63
	# Oil Price             0.21
	# Contact Email         rshintani@gmail.com
	# Gallons Collected     64.0
	# Expected Income       2.976
	# Quality (0 - 100):    4
	# Expected Donation     1.1904
# --------------------  --------------------------

# Make sure you can import everything
mods = 1
while mods == 1:
	try:
		from tabulate import tabulate #makes the nice tables
		import os.path #pathfinder
		import time #this is for any delays I want
		import sys
		import os
		from os import listdir
		import csv
		import urllib
		import urllib2
		from bs4 import BeautifulSoup           # pip install BeautifulS
		from datetime import date
		from file_keeper import *
		from interfaces import *




	except ImportError as err:
		print "Something didn't work right.\n"
		print "You don't have all the required modules on this computer."
		print  err.args

	mods = 0

# Check which OS is running and set the location for the main directory

if sys.platform.startswith('darwin'):
	print ""
	print "This is not a Linux, it's a Mac so you're going to get lost on the keyboard."
	print "It would be cool if you could actually specify if it's Robby or Mike too\n"

	runtime_dir = os.path.expanduser( "~/GDrive/cres_sheets" )  #mac
	print "Locfile: ", runtime_dir, '\n'
	# sheets = [ f for f in listdir(locfile)   ]
	# sheets.remove('.DS_Store') # Not sure what this is but we don't want it.

elif sys.platform.startswith('linux'):
	print ""
	print 'This is a Linux\n' 
	runtime_dir = os.path.expanduser( '~/cres_sheets2')
	print "Locfile: ", runtime_dir, '\n'
	sheets = [ f for f in listdir(runtime_dir)]

record = Keeper(runtime_dir)
interface = GUI()


