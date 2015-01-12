#!/usr/bin/python
import csv
from tabulate import tabulate
import os.path
from datetime import datetime
import urllib2
# this can be deleted

locfile = "/Users/AsianCheddar/Desktop/Python/location_list.csv"
opener = open(locfile)
handle = csv.DictReader(opener, dialect = 'excel', skipinitialspace = True)
head = handle.fieldnames
print ""
print head
print ""

# This program should make and use classes to store restaurnt information

class location(object):
	def __init__(self, name, address, city, state, zip_code, contact_person, phone_num ):
		self.name = name
		self.address = address
		self.city = city
		self.state = state
		self.zip_code = zip_code
		self.contact_person = contact_person
		self.phone_num = phone_num

	def info(self):
		out = [str(self.name).replace("\xe2\x80\x99", "'") , self.address, self.city, self.state, self.zip_code]
		return out 



	# makes a string for the googlemaps link
	def waypoint(self):
		destination = str(self.address) + str(self.city) + str(self.state) + str(self.zip_code)
		destination = destination.replace(' ' , '%20')
		return destination
		
	

# Takes two ints as input, looks up those indicise and makes a complete trip from 1 -> 2
def link_build(choice1, choice2):
		prefix = "https://maps.googleapis.com/maps/api/directions/json?origin=" 
		middle = "&destination="
		appendix = "&departure_time=now&key="


		start = str(list_of_locations[choice1].waypoint()  )
		destination = str(list_of_locations[choice2].waypoint()  )
		link = prefix + start + middle + destination + appendix
		return link



list_of_locations = {}


count = 0 
for place in handle:
	list_of_locations[count] = location(place["Name"], place["Street Address"], place["City"], place["State"], place["Zip"], place["Contact_Person"], place["Distance"])
	count = count + 1

# Ok so this class is set up
# Now I need to read the csv file and "import" the contents to the class...
# print list_of_locations[2].info()


print ""

# This is how to build a link:

# print link_build(1,2)


ro = 0
for location in list_of_locations:
	print location + 1 , list_of_locations[ro].info()
	
	ro = ro + 1
print ""

print "Where would you like to start?"

pick1 = int(raw_input())

print "Where would you like to go next?"
pick2 = int(raw_input() )

print link_build(pick1, pick2) 

# new_place.info()



opener.close()
