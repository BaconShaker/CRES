#!/usr/bin/python

# This version can add a location to the master csv file, 
# plan a route and display the entire trip's directions. 
# v.1 should try breaking up the trip into many trips so as to make
# running the add stats (location_mod2.py) program at each location.   



import csv 
import os.path
from datetime import datetime
import urllib
import urllib2
from bs4 import BeautifulSoup
import os
from tabulate import tabulate
import json



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
locfile = "/Users/AsianCheddar/Desktop/Python/location_list.csv"
# print locfile
	# Mike:

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
	"Get Directions to specific location",
	"Build Route by hand", 
	"Do a Pickup/Run route?",
	"Use Dist_calc to build a Route",
	"See Stats",
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

name_list = ["End Route"  ]
for location in locations:
	name_list.append(location['Name'])


# Set up functions, all inputs are assuming the var_file has already been opened:
# ie, input=header, when header=csvread()...

def check_sheet_exists(sheet):
	if os.path.exists(sheet):
		# print "Path works!" 
		print sheet 
		# print ""
		# print ""

	else: 
		print "The file you were looking for in " + sheet 
		print "Does not exist"
		print ""
		print ""



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
def link_build(locfile, stops, *args):
	

	os.system('clear')
	
	# Need to add ICNC to places... CHeater.

	#places.insert(0, "Industrial Council of Nearwest Chicago Incubator")

	# Need to get stops to be a leg[start ,stop]




	
	print "Here are the legs of the route you planned route: (make it so you can change a leg)"
	print ""
	print ""
	# print beg
	# print end
	print tabulate(stops, headers = ['Leg #','FROM --> TO', ""]) 
	print ""
	print ""
	print "stops: " 
	print stops

# Takes two ints as input, looks up those indicise and makes a complete trip from 1 -> 2

	prefix = "https://maps.googleapis.com/maps/api/directions/json?origin=" 
	middle = "&destination="
	appendix = "&departure_time=now&key="


	start = str(list_of_locations[stops[0][2] - 1 ].waypoint()  )
	destination = str(list_of_locations[stops[1][2] - 1 ].waypoint()  )
	link = prefix + start + middle + destination + appendix
	





	# Open LINK and return mapinfo
	handle = urllib2.urlopen(link)
	handle2 = handle.read()
	mapinfo = []
	mapinfo.append(json.loads(str(handle2)))

	handle.close()



	return mapinfo
	


def directions(mapinfo):

	directions = {
		"" : ""
	}
	for pam in mapinfo:
		steps = pam["routes"][0]['legs'][0]['steps']
		print ""

		leg_distance = pam["routes"][0]['legs'][0]['distance']['text']
		leg_time = pam["routes"][0]['legs'][0]['duration']['text']
		print "Distance: " + leg_distance
		print "Travel Time: " + leg_time
		print ""

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

		# for jedi in display:
		# 	print display[jedi]
		
		tabs = ["Turn", "Distance", "Instruction"]

		tab = tabulate(display, headers = tabs)

		print tab
		print ""
		print "Add in 'you have arrived @' markers?"



def build_route(hfi):
	point = 0
	add_waypoint = 0
	waypoints = []
	final_route = []
	while add_waypoint == 0:
		
		pie = tabulate(waypoints, headers = ['Stop #','Location Name']) 
		crust = what_to_do(name_list, "Choose a wayopint: " , pie, 0)

		
		if crust[0] == 0:
			
			for index, way in enumerate(waypoints):
				final_route.append([index + 1, way[1], way[0]])

			print "End of the loop"
			add_waypoint = 1

		else: 
			waypoints.append( crust )
			add_waypoint = 0
			point += 1

		
		# print ""
		# print "You have " + str(len(waypoints) + 1) + " waypoints."
		# print "Would you like to add another waypoint?"
		# print '[BLANK] = yes ; [ANYTHING] = no' 
		# print ""
		# if raw_input() != "":
		# 	add_waypoint = 1
		# else:
		# 	add_waypoint = 0
	return final_route

	



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



# THIS IS WHERE THE MAGIC HAPPENS!!!
before = "Hello, here is a list of what I can do..."
after = "Select a number from the list above. [BLANK] will quit."

choice = what_to_do(main_menu, before, after, 4)

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
	directions(leg)





read_locations.close()








