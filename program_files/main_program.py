#!/usr/bin/python
#/Users/AsianCheddar/the_matrix/bin/python
#/usr/bin/python

# This is the MAIN PAGE for the CRES Program.

# Functionality should include:
# 	Building a pickup route
# 		Run the route
# 		Add Data to CSV files
# 		Send pickup notices/reciepts 
# 			prior to pickup? 
# 			post collection results
# 	Browsing client/location details/statistics
# 		Provide to website?


# Cheating...
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



	except ImportError as err:
		print "Something didn't work right.\n"
		print "You don't have all the required modules on this computer."
		print  err.args

	mods = 0


# These Classes are imported from CRES folder, whereever it may be. 
from routebuilder import *
from collection import *
from msg_reciept2 import *
from file_writer import *

# First let's check which system is running.
	# Need to find a way to get the GDrive file on the the Linux side of things. That's going to be hard

# -----------------------------------------------------------------

if sys.platform.startswith('darwin'):
	print ""
	print "This is not a Linux, it's a Mac so you're going to get lost on the keyboard."
	print "It would be cool if you could actually specify if it's Robby or Mike too\n"

	locfile = os.path.expanduser( "~/GDrive/cres_sheets" )  #mac
	print "Locfile: ", locfile, '\n'
	# sheets = [ f for f in listdir(locfile)   ]
	# sheets.remove('.DS_Store') # Not sure what this is but we don't want it.

elif sys.platform.startswith('linux'):
	print ""
	print 'This is a Linux\n' 
	locfile = os.path.expanduser( '~/cres_sheets2')
	print "Locfile: ", locfile, '\n'
	sheets = [ f for f in listdir(locfile)   ]


# -----------------------------------------------------------------

record = Keeper(locfile)
record.update_donation_total()

options = [record, record.all_names(), record.master_lister()]
# record.update_donation_total()
route_master = Route(options, locfile)

# This is where you'd need to start a loop to make it so you can quit at the first screen
the_route = route_master.build()
if len(the_route) == 0:
	menu2 = 'skip'
	print "You didn't add anything to the route! ROUTE LENGTH: ", len(the_route)

else:
	menu2 = ""


while menu2 != "skip":
	user_inputs = route_master.run_route() # This is the user inputs from the collection GUI!

	print "\n\nThis is what routemap.build() returns:\n" , tabulate(the_route)

	print '\nUSER INPUTS: ' , user_inputs , '\n'

	# Essentially, collections is a list of dictionaries created by the Collection class.
	# Each dict gets turned into a Collection by run().
	collections = [ Collection(leg).run() for leg in user_inputs ]

	print "\n\nReciepts for collections:"

	all_sent = 0

	# The control list for the email reciept is in Mailer
	# Mailer sends emails to everyone about the pickup
	for collection in collections:
		print "\nEmail sent to: " , collection["Contact Person"] , "at" , collection['Contact Email']
		print tabulate(  [ ( key , collection[key] ) for key in collection  ]  )

		print "Choices are q, back, [anything, y, yes] = next"
		sure = raw_input( "\n Send? ")

		if sure == 'y' or sure == 'yes' or sure == '':
			all_sent += 1 
			


		elif sure == "back" or sure == 'b' or sure == 'n': 
			break

		elif sure == "q" or sure == 'quit':
			menu2 = "skip"
			break

	if all_sent == len(collections):
		menu2 = "skip"
		# send = [ Mailer(collection).send_reciept() for collection in collections ]
		print "\nAll the receipts were sent successfully!\n"
		record.write_pickups_csv( collections )
		# record.update_donation_total()


	else:
		print "\n" , menu2
		print "Not all of the receipts were sent and you got spit back to the inputs menu or quit"


	
# Need to take each collect in collections and grab only the info we want to 
# get mailed to the restaurants  


print "\n\n\n\nThis is the end of Main Program"




