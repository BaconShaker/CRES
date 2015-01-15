#!/usr/bin/python

# This version can add a location to the master csv file, 
# plan a route and display the entire trip's directions. 
# v.1 should try breaking up the trip into many trips so as to make
# running the add stats (location_mod2.py) program at each location.   


# 		Get directions to specific place
# 		Build a Route by hand 
# 			Return directions
# 			Provide method for inputting heights while on Route 
# 		Make_Route by distance calculator
# 		See Stats for each restaurant
# 			Duration since last pickup
# 				Time of year 
# 			Height since last pickup
# 			Score
# 			Difficulty/Collectability
# 		Compare Stats for all locations
# 		Edit location info

# When the usr is on a route, provide 
# 	directions
# 	stat update raw_input

# Update a master file on the server every ___ days


import csv 
import sys 
import operator # This is for what? Something in the arrange_locations() def
import os.path
from datetime import datetime
import urllib
import urllib2
from bs4 import BeautifulSoup
import os
from tabulate import tabulate
import json


# This is a feeble attempt to figure out which computer I'm on
# The goal here is to get this program to work on any computer easily given 
# the files are all on the cloud somewhere. 

# Get all the files
# this_path = os.system('pwd')
# /home/robby/Desktop/Python
# print this_path --> 0
# Should be /home/root/python on Edison, 

# this_path = os.path.abspath()

# Set up URL's:

# Set up FilePaths
	# Robby:
# pickups = this_path + "/pickups.csv"
# locfile = this_path + "/location_list.csv"

# pickups = "/home/robby/Desktop/Python/pickups.csv"
if sys.platform.startswith('darwin'):
	print ""
	print "This is not a Linux, it's a Mac so you're going to get lost on the keyboard."
	print "It would be cool if you could actually specify if it's Robby or Mike too\n"

	locfile = "/Users/AsianCheddar/Desktop/Python/location_list.csv" #mac
	print "Locfile: ", locfile, '\n'

elif sys.platform.startswith('linux'):
	print ""
	print 'This is a Linux\n'
	locfile = '/home/robby/Desktop/Python/location_list.csv' 
	print "Locfile: ", locfile, '\n'

# locfile = '/home/robby/Desktop/Python/location_list.csv' 
# locfile = "/Users/AsianCheddar/Desktop/Python/location_list.csv" #mac
# print locfile
	# Mike:

# Need to rearange the csv file here before anything else needs it!

def arrange_locations(sheet):
	if os.path.exists(sheet):
		print "Path works!" 
		change = open(locfile)
		data = csv.DictReader( change , dialect = 'excel')

		sorted_list = sorted(data, key = lambda row: row['Name'] )

		# print "Sorted list: ",  sorted_list
		
		new_file = open( locfile , 'wb')
		writer = csv.DictWriter(new_file, fieldnames = data.fieldnames)
		writer.writeheader()
		for row in sorted_list:
			# print "Row: " , row
			writer.writerow(row)

		# Works for the most part, just need to get it to delete the old rows before replacing them with the new ones
		# Then need to check if it works with the directions
		change.close()
		new_file.close()

	else: 
		print "The file you were looking for in " + sheet 
		print "Does not exist"
		print ""
		print ""

arrange_locations(locfile)

# Settings: 
spacing = 2
spacing = int(spacing)

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

	def list_name(self):
		return self.name.replace("\xe2\x80\x99", "'")


	


	# Make a pickup and add input to that location's csv file
# class pickup(object):
# 	def __init__(self, location, gallons, leftover, pounds, score, date, time):
# 		self.location = location
# 		self.gallons = gallons
# 		self.leftover = leftover
# 		self.pounds = pounds
# 		self.score = score
# 		self.date = date
# 		self.time = time

# 	def info(self):



# Set up a list of locations to use in the tabs
list_of_locations = {}
count = 0 
for place in handle:
	list_of_locations[count] = location(place["Name"], place["Street Address"], place["City"], place["State"], place["Zip"], place["Contact_Person"], place["Distance"])
	count = count + 1


main_menu = [
	"DEFAULT",
	"Add Location", 
	"Edit Location info",
	"Delete Location",
	"Set up Route; Get Directions",
	"Build Route by hand", 
	"Do a Pickup/Run route?",
	"Use Dist_calc to build a Route",
	"See Stats",
	"List",
]

# Set up oil as DictReader
new_oil = {
	"":"",
}


# open files and set global dicts, lists and strings to manipulate later
read_locations = open(locfile)


# read_pickups =  open(pickups)
locations = csv.DictReader(read_locations, dialect = 'excel', skipinitialspace = True)
location_stats = locations.fieldnames



name_list = [  ]
for location in locations:
	name_list.append(location['Name'])
	# name_list.sort()
	# sorts the names just fine, but the indicies don't change so you make the wrong choices... 
name_list.insert(0 , "End Route")



# Set up functions, all inputs are assuming the var_file has already been opened:
# ie, input=header, when header=csvread()...




# Going to need a csv file for every location 
# To hold the data for individual pickups



# ------------------------------------------------------------------------

# Start by asking what usr wants to do.
def what_to_do(abilities, before, after, default_choice, *args):
	os.system('clear')
# Returns a number corresponding to the response ability[index] in the list below. 


	# abilities = [ HAS BEEN MOVED TO GLOBAL
	# 	"Add Location", 
	# 	"Edit Location info",
	# 	"Delete Location",
	# 	"Get Directions to specific location", 
	# 	"Build Route by hand", 
	# 	"Use Dist_calc to build a Route",
	# 	"See Stats",
	# 	]

	looper = 0
	while looper == 0:
		print before
		print ""
		count = 0
		counter = [0,]
		for ability in abilities:
			print "		" + str(count) + "	" + str(ability)
			counter.append(int(count))
			count = count + 1

		print ""
		print "** Default is set to [" + str(default_choice) + "]"
		print ""
		print after

		choice = raw_input()


		if choice == "":
			choice = default_choice
		else:
			choice = int(choice)


		if choice not in counter:
			looper = 0
			os.system('clear')

		else:
			print ""
			choice = choice + 0
			word =  abilities[int(choice)]
			print "You picked: [" + str(choice) + "]  " + str(word)
			word = word.replace("\xe2\x80\x99" , "'")
			response = [ int(choice), word] 
			return response
			looper = looper + 1
			



# ------------------------------------------------------------------------
def add_location(cols, *args):
	os.system('clear')

	keep_adding = 0
	count = 0
	while keep_adding != "n":
		print "You have chosen to add a new location to the master file."
		print location_stats
		print ""
		new_locations = {}

		print "What is the FULL name of the restaurant you would like to add?"
		new_locations["Name"] = raw_input("  ")
		print ""

		print "What is the NICKNAME you would like to assign this location?"
		new_locations['Nickname'] = raw_input("  ")
		print ""

		print "What is the street address of location to be added?"
		print "Eg: 2021 W Fulton"
		new_locations['Street Address'] = raw_input()
		print ""
		print "Make it able to go back to fix mistakes"
		print "What city is the location in? [Blank] = Chicago" 
		bb = raw_input() 
		if bb == "":
			new_locations['City'] = "Chicago"
		else: 
			new_locations['City'] = bb
		print ""

		print "What is the State? [BLANK] = IL"
		aa = raw_input() 
		if aa == "":
			new_locations['State'] = "IL"
		else: 
			new_locations['state'] = aa
		print ""

		print "What is the Zip?"
		new_locations['Zip'] = raw_input("	")
		print ""

		print "And lastly, who beith the Contactuth Personath?"
		new_locations['Contact_Person'] = raw_input("	")
		print ""

		print "Here is what you just entered, if it is correct hit [ENTER]"
		print ""
		new_row = []
		for key in new_locations:
			print key + ": " + new_locations[key]
			new_row.append(new_locations[key])

		print ""
		if raw_input() == "":
			locations = open(locfile, 'a')
			writer = csv.DictWriter(locations, fieldnames = location_stats)
			writer.writerow(new_locations)
			locations.close()
			print ""

		print "Would you like to add another location right now? [Y/n]"
		print ""
		keep_adding = raw_input()
		
	

	return new_locations


# ------------------------------------------------------------------------
def link_build(locfile, route, *args):
	
	os.system('clear')
	
	# Need to add ICNC to places... CHeater.

	#places.insert(0, "Industrial Council of Nearwest Chicago Incubator")

	# Need to get stops to be a leg[start ,stop]
	beg = [ loc[2] for loc in route ]
	end = [ loc[2] for loc in route ]

	beg.pop()
	end.pop(0)
	print beg, end

	legs = zip(beg, end)

	name1 = [ loc[1] for loc in route ]
	name2 = [ loc[1] for loc in route ]

	name1.pop()
	name2.pop(0)

	legs2 = zip(name1, name2)

	print 'legs2: ', legs2
	
	print "Here are the legs of the route you planned: (make it so you can change a leg)"
	print ""
	print ""
	# print beg
	# print end
	print tabulate(legs2, headers = ['FROM -->', "TO"]) 
	print ""
	print ""
	print "starts: " , beg

	print "stops: ", end
	print ""
	print "legs: ", legs

# Takes two ints as input, looks up those indicise and makes a complete trip from 1 -> 2

	prefix = "https://maps.googleapis.com/maps/api/directions/json?origin=" 
	middle = "&destination="
	appendix = "&departure_time=now&key="

	links = []
	hockey = 0 # This is just a counter

	for leg in legs:
		print "leg: " , leg

		start = str(   list_of_locations[ leg[0] - 1 ].waypoint()  )
		destination = str(   list_of_locations[leg[1] - 1 ].waypoint()  )
		link = prefix + start + middle + destination + appendix
		links.append(link)
		hockey += 1

	# print "links: ", links
	print ""
	mapinfo = []

	for link in links:
		# Open LINK and return mapinfo
		handle = urllib2.urlopen(link)
		handle2 = handle.read()
		
		mapinfo.append(json.loads(str(handle2)))

		handle.close()


	# print mapinfo
	return mapinfo
	

# This bad boy handles the directions' parsing fron json to readable text. 
def directions(mapinfo, flightplan):

	directions = {
		"" : ""
	}

	start_address = [ pam["routes"][0]['legs'][0]['start_address'] for pam in mapinfo ]
	end_address = [pam["routes"][0]['legs'][0]['end_address'] for pam in mapinfo ]

	rob = 0     # Just an old fashioned counter... Counts for each waypoint. 0 is START


	for pam in mapinfo:
		# print "\n" * 5
		steps = pam["routes"][0]['legs'][0]['steps']

		display = []
		turn = 0
		leg = 0
		for step in steps:
			to_go = step['distance']['text']
			turn = turn + 1
			words = step['html_instructions']
			words = words.replace( '<b>' , ' ')
			words = words.replace( '</b>' , ' ')
			words = words.replace( '<div style="font-size:0.9em">' , '')
			words = words.replace( '</div>' , ' ' )

			display.append([turn,  to_go, words])



			# print str(turn) + "	" + words + " (" + to_go + ")"

		
		# Display each leg's directions in a spreadsheet
		tabs = ["Turn", "Distance", "Instruction"]
		tab = tabulate(display, headers = tabs)
		# print tab
		# MOved that down a few lines so I could make the output look pretty
		

		start_name = flightplan[rob][1]
		end_name = flightplan[rob + 1][1]


		# Make a better display for the to and from on each directions section
		# print flightplan
		# quick = tabulate( [ start_address[rob], end_address[rob] ] , headers = [ str(start_name), str(end_name) ] )
		# print quick
		print "****************************************************************************"
		print "****************************************************************************"
		print ""
		print "			THIS IS WAYPOINT #" , rob + 1  
		print '\n' * 3

		print 'Starting at: ' , start_name
		print '             ' , start_address[rob]
		print ""
		print tab
		print ""
		print 'Ending at :  ' , end_name
		print '             ' , end_address[rob]

		# This block converts time and dist json to strings for a clean tabulate below
		leg_distance = pam["routes"][0]['legs'][0]['distance']['text']
		leg_time = pam["routes"][0]['legs'][0]['duration']['text']
		# print "dist_together: " , dist_together
		# print "time together: " , time_together
		print ""

		print 'Use leg_distance to calculate fuel surcharge'
		print ""
		ref = tabulate( zip([leg_distance], [leg_time]), headers = ["Leg Distance", "Travel Time"] , tablefmt = 'grid')
		print ref
		# print flightplan
		# print 'Address: ', start_address[rob]
		# print "End address: ", end_address[rob]


		rob += 1
		print ""
		print 'This is where the loop for doing a pickup should go.'
		print "\n" * 3

		
def build_route(not_used):
	point = 0
	add_waypoint = 0
	waypoints = []
	final_route = []
	while add_waypoint == 0:
		
		pie = tabulate(waypoints, headers = ['Stop #','Location Name']) 
		crust = what_to_do(name_list, "Choose a wayopint: " , pie, 0)

		
		if crust[0] == 0:
			
			for index, way in enumerate(waypoints):
				final_route.append( [index + 1, way[1], way[0] ])

			print "End of the loop"
			add_waypoint = 1

		else: 
			waypoints.append( crust )
			add_waypoint = 0
			point += 1

	return final_route

	



# -----------------------------------------------------------------------------------------------------------------
# First, make sure the csv file exists, read it then make sure it's arranged in alphabetical order before moving forward
# If possible, try to keep "ICNC" the top location. 

# arrange_locations(locfile)

# THIS IS WHERE THE MAGIC HAPPENS!!!
default = 6
before = "Hello, here is a list of what I can do..."
after = "Select a number from the list above. DEFAULT: [" + str(default) + "] " + main_menu[default]

choice = what_to_do(main_menu, before, after, default)

print str(choice) + " IS what you picked"

if choice[0] == 1:
	print ''
	added = add_location(location_stats)
	print "Maybe someday this will tell you what you just added,"
	print "but for the time being you're going to have to open the file"
	print "and check if you got everything right. "
	print added


elif choice[0] == 4:
	# Get Directions to a specific place, shouldn't be too hard eh?
	
	route = build_route(32)
	print "This is the input to link_build: ", route				
	
	# Make list from Route then pass it to link_build to make the link
	# link_build returns mapinfo in jason format... 
	# save it to leg then pass json to directions which just tabulates 
	# and makes it pretty lookin
	leg =  link_build(locfile, route)
	directions(leg, route)

elif choice[0] == 9:
	print "\n", "Here's a list, like you asked! " , '\n'
	rocks = len(list_of_locations)

	print  "There are" , rocks , "locations in the location_list." , '\n'

	loc1 = [list_of_locations[i].list_name() for i in range(rocks)]
	loc2 = [i for i in enumerate(loc1)]
	contents = tabulate(loc2, headers = ['#', 'Location'])
	print contents , '\n'

elif choice[0] == 6:
	print "Ace"
	# This section should simulate a pickup and add the resuts to the corresponding location file
	



read_locations.close()


# This is the end





