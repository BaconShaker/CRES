#!/envs/CRES/bin/python

# This is the Location class. 
# 	It should be able to return simple statistics and information
# 	based on a location's name only.	

import os
import mysql.connector
from datetime import *
from tabulate import tabulate
from data_manager._get_credentials import *
from oauth2client.client import SignedJwtAssertionCredentials
from oauth2client import client
from oauth2client import tools
import oauth2client
from apiclient.discovery import build
from data_manager.__init__ import __mike__
import sys, getopt
from string import Template

db = mysql.connector.connect(**__mike__)
cursor = db.cursor()
print "Logged in as Mike\n"

def getDetails(forLoc):
	sql = Template("""SELECT 
				Name,
				Address,
				Zip,
				City,
				Charity,
				Contact,
				`Last Pickup`,
				`Next Pickup`,
				`Next Pickup Gallons`,
				`Average Collection`,
				Email, `Phone Number`,
				Dumpster, `Average Donation`, `Total Donation`,
				`Fill Time Gallons`, `Fill Time`, `Total Gallons`
				FROM Locations
				WHERE Name LIKE "$location%" """)
	sql = sql.substitute(location = str(forLoc))


	cursor.execute(sql)
	fields = map(lambda x:x[0], cursor.description)
	result = [dict(zip(fields,row))   for row in cursor.fetchall()]
	try:
		return result[0]
	except IndexError:
		print "You forgot to specify a location!\n 	 Need -n <Location>"
		sys.exit()

def getCollections(nameToLookup):
	sql = """SELECT 
			`Pickup Date`, 
			`Gallons Collected`,
			`Expected Revenue`,
			`Expected Income`,
			`Expected Donation`
		FROM Pickups
		WHERE `Location` = '%s'
		ORDER BY `Pickup Date`""" % (nameToLookup)
	cursor.execute(sql)
	fields = map(lambda x:x[0], cursor.description)
	results = [dict(zip(fields,row)) for row in cursor.fetchall()]
	try:
		return results
	except IndexError:
		print "You forgot to specify a location!\n 	 Need -n <Location>"
		sys.exit()


def monthlySummary(restaurantName):
	sql = """SELECT 
			monthname(`Pickup Date`) as 'Month', 
			`Gallons Collected`,
			`Expected Revenue`,
			`Expected Income`,
			`Expected Donation`
			FROM Pickups
			WHERE `Location` = '%s'
			GROUP BY monthname(`Pickup Date`)
			ORDER BY  `Pickup DATE`""" % (restaurantName)
	cursor.execute(sql)
	fields = map(lambda x:x[0], cursor.description)
	results = [dict(zip(fields,row)) for row in cursor.fetchall()]
	try:
		return results
	except IndexError:
		print "You forgot to specify a location!\n 	 Need -n <Location>"
		sys.exit()


class Location():
	def __init__(self, locationName):
		print "This is the Location Class"
		
		if len(locationName) == 0:
			print "\nYou didn't include any arguments, try -h for options.\n"
			print "This should list all the last pickups."
			sys.exit()
		else:
			self.info = getDetails(locationName)
		


	def monthlyReport(self):
		print "			List of ALL Collections for", self.info['Name']
		self.collections = getCollections(self.info["Name"])
		print tabulate( self.collections, headers = "keys")

	def yearlyReport(self):
		print "	This is a MONTHLY summary for", self.info["Name"]
		monthlys = monthlySummary(self.info['Name'])
		print tabulate(monthlys, headers = "keys")




def main(argv):
	searchFor = ""
	createReport = False
	yearlyReport = False

	try:
		opts, args = getopt.getopt(argv, "hn:vM", ["--location=", "--collections", "--monthly"])
	except getopt.GetoptError:
		print "_Location -n <Location Name>"
		sys.exit(2)
	
	for opt, arg in opts:
		if opt == "-h":
			print "You need to specify a Location to look up!\n"
			print "	-n 	Location_Name"
			print "	[-v] 	Prints ALL Location Collections"
			print "	[-M] 	Prints Monthly summary"
			sys.exit(2)
		elif opt in ("-n", "--location"):
			searchFor = arg
		elif opt in ("-v", "--collections"):
			createReport = True
		elif opt in ("-M", "--monthly"):
			yearlyReport = True


	loc = Location(searchFor)

	print "\n\n"

	# Filter out the extra colums returned
	# I did it this way so other scripts can use _Location.info
	# and will get all of the information, not just this list.

	toDisplay = ["Average Collection",
				"Average Donation",
				"Charity",
				"Contact",
				"Email",
				"Fill Time",
				"Fill Time Gallons",
				"Last Pickup",
				"Next Pickup",
				"Next Pickup Gallons",
				"Phone Number"]


	disp = [(key , loc.info[key] ) for key in toDisplay]
	print "	Quick Info for:", loc.info["Name"]
	print tabulate(disp)

	

	if createReport:
		print "\n\n"
		loc.monthlyReport()
	else:
		pass

	if yearlyReport:
		print "\n\n"
		loc.yearlyReport()
		

	
	
	# print loc.gallonsCollectedByYear()
	# print loc.routes()




if __name__== '__main__':

	main(sys.argv[1:])

	# Need to make it so it takes abbreviated names not just full names 


	