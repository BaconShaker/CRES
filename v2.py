#!/usr/bin/python


# This is the second coming of the Jedi Order, v2.py.

# The idea here with v2 is basically mimic v1 in terms of program structure, 
# and change the file structure so instead of having one file to rule all other files, 
# we have one file and we just read the names to make the lists. 

# CRES
# 	-- Location 1 
# 		-- Detail 1
# 		-- Detail 2 
# 	-- Location 2 
# 		-- ..

# Also, you need to make sure the files that ARE NOT ON GITHUB (ie the location files)
# can all be found in '~/Locations'

# And in general clean things up a bit now that I know how Python Gooder. 


# So first, let us go and Import some libs and stuffs. 



import csv 
import sys 
import operator # This is for what? Something in the arrange_locations() def
import os.path
from os.path import isfile, join
from datetime import datetime
import urllib
import urllib2
from bs4 import BeautifulSoup
import os
from os import listdir
from tabulate import tabulate
import json
from collections import defaultdict



# print "We are also going to need some packages..."
# for key in sys.modules():
# 	print key
# That will list the Imported Modules for you. 

# Now let's check which system is running 

if sys.platform.startswith('darwin'):
	print ""
	print "This is not a Linux, it's a Mac so you're going to get lost on the keyboard."
	print "It would be cool if you could actually specify if it's Robby or Mike too\n"

	locfile = os.path.expanduser( "~/GDrive/cres_sheets" )  #mac
	print "Locfile: ", locfile, '\n'

elif sys.platform.startswith('linux'):
	print ""
	print 'This is a Linux\n' 
	locfile = os.path.expanduser( '~/Locations')
	print "Locfile: ", locfile, '\n'


# The first thing we're going to have to do is find the 
# file with all the locations in it. 
# Which should be easy if we put it in the right place.
# Then let's make a list of all the locations for the menu.

# locations = [location for location in locfile]
# print locations

# sheets is a list of files in locfile
sheets = [ f for f in listdir(locfile)   ] 


print "Unsorted: ", sheets, '\n'

# Use the .remove here to get rid of entries we don't want to make the list. 
sheets.remove('.DS_Store')
sheets.remove('master.csv')
print "Censored: ", sheets, '\n'
sheets.sort()
print "Sorted: ", sheets, "\n"

# -------------------------------------------------------------------
# Given choices, what_to_do will print before, choices then after
# in a menu form and will return the [selection, words from the selection] 

def what_to_do(choices, before, after, default_choice, *args):
	# Returns a number corresponding to the response choices[index] in the list below. 
	os.system('clear') 	
	looper = 0	
	while looper == 0:
		print "\n" , before
		print ""
		count = 0
		counter = [0,]
		for choice in choices:
			choice = choice.decode('utf-8')
			print "		" + str(count) + "	" + str(choice)
			counter.append(int(count))
			count = count + 1
		print ""
		print "** Default is set to [" + str(default_choice) + "]"
		print ""
		print after
		selection = raw_input()
		if selection == "":
			selection = default_choice
		else:
			selection = int(selection)
		if selection not in counter:
			looper = 0
			os.system('clear')
		else:
			print ""
			# choice = choice + 0   # I think this can be deleted
			word =  choices[int(selection)]
			print "You picked: [" + str(selection) + "]  " + str(word)
			# word = word.replace("\xe2\x80\x99" , "'")
			response = [ int(selection), word] 
			return response
			looper = looper + 1

# -----------------------------------------------------------------

class Restaurant:
	def __init__(self, master, **kwargs):
		self.name = master['Name']
		self.address = master['Address']
		self.city = master['City']
		self.state = master['State']
		self.zip_code = master['Zip']
		self.contact_person = master['Contact_Person']
		self.phone_num = master['Phone_Number']

	# Make a function that shows the header(s) of the csv's

	# Going to need to read the names of the CSV's then add it to the Restaurant Object
	# Also going to need to opn each file to get the actual information to add it to the Object

	def get_names(self):
		# Should probably check if the file exists already... I'll come back to this. 

		pass


# -----------------------------------------------------------------



def make_locations(locfile):

	# Here is the list that controls the headers on the pickup_files
	pickup_heads = []

	# Open the master file and get the nicknames. The Nicknames will become the individual
	# filenames for the pickup files. 

	apple = open(locfile + '/master.csv')
	oranges = csv.DictReader(apple, dialect = 'excel', skipinitialspace = True)

	nicknames = [x['Name'] for x in oranges]

	for nick in nicknames:
		pickup_file = locfile + '/' + nick + '.csv'
		if os.path.exists(pickup_file):
			print "there's a file for: " , nick

		else:
			print "There is no '" ,  pickup_file   , "' we should make one!\n" 
			to_make = open( pickup_file, 'a' )
			writer = csv.DictWriter( to_make , fieldnames = pickup_heads)
			writer.writeheader()
			to_make.close() 
	return nicknames
	apple.close()


# -----------------------------------------------------------------



def class_loader(master_dir):
	
	projects = defaultdict(dict)
	
	handler = open(master_dir + '/master.csv')
	master_read = csv.DictReader( handler )
	
	headers = master_read.fieldnames
	for rowdict in master_read:
		if None in rowdict:
			del rowdict[None]
		name = rowdict.pop("Name")
		address = rowdict.pop('Street Address')
		projects[name][address] = rowdict

	return projects
	handler.close()




# -----------------------------------------------------------------


	# Looks up all the .csv files in cres_sheets, strips the extensions 
	# and compares the names to the choice made.

	# Need to make the individual .csv's have the same headers and get imputs
	# from pickups.py. 

def show_details(location, locfile):
	
	
	fo = open(locfile + '/' + location + '.csv' )
	fr = csv.DictReader(fo, dialect = 'excel', skipinitialspace = True)

	# heads = fr.fieldnames
	# print fr.iteritems
	new_fr = []
	print ""
	count = 0
	to_show = [ 'pickup_count' , 'leftovers', 'score' , 'gallons_collected' , 'price' , 'income' , 'to_charity'  ]
	for row in fr:
		new_fr.append( { key.replace( '_' , ' ') : value for key, value in row.items() if key in to_show} )
 		count += 1
	# print '\n' * 10
	# print 'New fr: ' , new_fr
	print "These are the stats for" , location , ':\n\n' 
	print tabulate(new_fr, headers = 'keys') , '\n\n\n\n'
	return tabulate(new_fr, headers = 'keys') , '\n\n\n\n'

	fo.close()


# -----------------------------------------------------------------


def run_pickup(spike):
	diesel = 'http://www.eia.gov/dnav/pet/pet_pri_gnd_dcus_r20_w.htm'
	ams = 'http://www.ams.usda.gov/mnreports/nw_ls442.txt'

	# File paths to look for:
	# Robby:
	pickups = "/Users/AsianCheddar/Desktop/Python/pickups.csv"
	locfile = "/Users/AsianCheddar/Desktop/Python/location_list.csv"
	# Mike:

	# Settings: 
	spacing = 2 # Gets used as an int later
	spacing = int(spacing)

	# Functions:

	def inches_cubed_to_gallons(inches3):
		inches3 = float(inches3) * 0.0043290
		return inches3

	def height_to_volume(height): 
		# Takes Height measured from bottom of tank to top of liquid and returns volume
		# dimensions of bin are: 36H x 28W x 48L
		h = 36
		w = 28
		l = 48
		volume = height * w * l
		gallons = inches_cubed_to_gallons(volume)
		return gallons

	def gallons_to_pounds(gallons):
		#weight of vegetable oil is 7.75lbs per gallon
		lbs = gallons * 7.75
		return lbs

	def price_lookup(pounds, ams):
		# Need to get work on this parser.  

		print ""
		print "Price_lookup():" # Input gallons or inches?
		print ""
		response = urllib2.urlopen(ams)
		# response = urllib2.urlopen('http://www.ams.usda.gov/mnreports/nw_ls442.txt')
		soup = BeautifulSoup(response)
		# page = response.readline()
		text = soup.get_text()
		print text[301:475]
		print ""
		# soup.prettify(formatter= 'html')

		# total = pounds * price
		# return total
		response.close()

	# GETS price from "diesel"
	def	get_a(grip):
		diesel = urllib2.urlopen(grip)
		soup = BeautifulSoup(diesel)
		# links = soup.find_all( "Current2")
		print "This is the price of Fuel today according to: ", diesel
		soup.prettify()
		data = soup.find_all('td' , 'Current2')
		length = len(data)
		# print data[13]
		temp = str(data[13])
		print temp
		price = temp[32:36]
		return price

		diesel.close()



	#---------------------------------------------------------------------------------------
	# First, clear the screen.

	os.system('clear')

	# Define locations for the menu
	sheets_two = [ sheet.replace( '.csv' , '' ) for sheet in sheets ]
	location_input = what_to_do(sheets_two, "Where would you like to run a pickup for?", 'Thank you!', 0)

	# Prompt for inputs (Loation, Height on Arrival, Height on Departure)
	inputs = {
		"location" : location_input[1]
	}
	print "\n" * spacing

	print "Height on Arrivial: [INCHES]\n"
	harrival = raw_input()
	print "\n" * spacing

	print "Height at Depature: [INCHES]\n\n\n"
	hdepart = raw_input()
	


	# I don't think this will work... yet, need to get hardware to make the inputs
	# just entering the time here will require decoding and too much time to be changed later anyway. 

	# print "What time did you arrive at ", location_input[1] , '?\n'
	# start_pickup_time = raw_input()

	# print "\n\nWhat time did you leave?"
	# end_pickup_time = raw_input()

	# So for now:
	print "How long did you spend at " , location_input[1] , '?\n 	FORMAT: [ hr.minutes ] --->  5.25 \n'
	pickup_duration = raw_input()
	print "\n\n"

	# Check inputs are correct
	print "This is what we have so far, are you sure you'd like to keep going?"
	print ""
	print "Location: " + inputs['location'] 
	print "Height on Arrival: " + harrival
	print "Height on Departure: " + hdepart
	print "Duration: " , pickup_duration
	print ""
	print "[YES/NO] This is where you should be able to get back to the last input to make changes... Haven't got that working just yet. "

	# Calculate volume -> pounds
	checker = raw_input().lower() 
	if checker != "n": 
		print "Well ok then, good luck going forward!"
		print "\n" * spacing
		gal_arrival = height_to_volume(float(harrival))
		gal_departure = height_to_volume(float(hdepart))
		score = round(((float(gal_arrival) - float(gal_departure)) / float(gal_arrival)) ,2) * 100
		gallons_collected = gal_arrival - gal_departure
		pounds_collected = gallons_to_pounds(gallons_collected)

	else:
		print "start over, don't pass go"


	# Calculate price using pounds

	# Look up AMS Price data
	price_lookup(pounds_collected, ams)

	print "Manually lookup the price and enter it here: [$cwt] Example, 23.34 \n\n"
	price = float(raw_input()) / 100.0
	flat_fee = 15.0 / 100.0 			# Here is where you change the flat fee
	print "Our flat fee is: 		It can be changed ~line 373"
	we_get = flat_fee * pounds_collected
	they_get = (price - flat_fee) * pounds_collected
	price_of_fuel = get_a(diesel) 

	# Start building inputs
	# Inputs is going to be the Dict that's RETURNed by this function. 
	inputs['height_on_arrival'] = harrival
	inputs['height_on_departure'] = hdepart
	inputs['score'] = score
	inputs['gallons_collected'] = round(gallons_collected, 2)
	inputs['pounds_collected'] = round(pounds_collected, 2)
	inputs['leftovers'] = round(gal_departure, 2)
	inputs['Pickup_Duration'] = pickup_duration
	inputs['income'] = round(we_get, 2)
	inputs['to_charity'] = round(they_get, 2) 
	inputs['price'] = price # of WVO
	inputs['fuel_price'] = price_of_fuel



	# Calculate Fuel Surcharge
	# Datestamp
	# End Loop
	# Display resulting Dictionary from inputs[]
	print "\n" * 100
	print "Here is a breakdown of how the pickup went."
	print ""
	print "Location visited: %(location)s" % (inputs)
	print "Oil collected: %(gallons_collected)s gallons" % (inputs)
	print "We only left ~ %(leftovers)s gallons behind" % (inputs)
	print ""
	print "The price today was: %(price)s $cwt" % (inputs)
	print "Meaning CRES gets to keep, $%(income)s" % (inputs)
	print "And the Charities get $%(to_charity)s" % (inputs)
	print ""
	print "For a score of: %(score)s" % (inputs)
	print ""
	print "The price of #2 Diesel today: $%s" % (price_of_fuel)
	print "Source: " + diesel


	print "These results will be added to the pickups.csv file above."
	print "Thank you for your cooperation, we hope you come back soon!"
	print ""
	for row in inputs:
		print str(inputs[row]).replace('_' , ' ') , "	" , row 


	return inputs
	

	

# -----------------------------------------------------------------


def add_to_csv(to_add):
	print "\n\nUSEAGE: add_to_csv( DICT to add )"
	print '\n\n\n\n'
	print to_add.keys()
	print ""
	print to_add
 	print '\n\n\n\n'
	# Figure out which location this info needs to be added to... 
	target_file = locfile + "/" + to_add['location'] + '.csv'


	print target_file
	print '\n\n\n\n'

	fop = open(target_file)
	fdr = csv.DictReader(fop, dialect = 'excel', skipinitialspace = True)


	pickup_count = 1

	for line in fdr:
		pickup_count += 1 
	print "This is pickup #:" , pickup_count

	to_add['pickup_count'] = pickup_count

	howlong_add = len(to_add.keys())
	howlong_fdr = len(fdr.fieldnames) 

	print "fdr: " , howlong_fdr
	print "to_add: " , howlong_add 

	if howlong_fdr == howlong_add:
		# This one only writes the INPUT ROW.
		fw = open(target_file, 'a')	
		writer = csv.DictWriter(fw, to_add.keys())
		writer.writerow(to_add)
		fw.close()

	else:
		# This overwrites the file completely, may be a good idea to make a script here that 
		# moves the file that's being replaced to a safe location?
		fw = open(target_file, 'wb')	
		writer = csv.DictWriter(fw, to_add.keys())
		writer.writeheader()
		writer.writerow(to_add)
		fw.close()

	fop.close()
	

# -----------------------------------------------------------------





# -----------------------------------------------------------------

# Let us start the Program here, methinks
# Load the restaurants into the class. 
name_list = make_locations(locfile)
name_list = [name.decode('utf-8') for name in name_list]
print "Name List: " , name_list

# robby = class_loader(locfile)
# print robby['Erie Cafe']['536 W. Erie Street']



main_menu = [ 
	'Exit',
	'List Restaurants',
	'Run a pickup',
	]	

main1 = "This is a list of what this program can currently do:"
main2 = "Looking to add more now so hold tight... \n"
main_menu_choice = what_to_do(main_menu, main1, main2, 0)


# re if pick below, 
# 	[0] is the number input from the prompt,
# 	[1] should be the string in 'word' from the list 


if main_menu_choice[0] == main_menu.index('List Restaurants'):

	default_choice = 0
	top = "Here's a list of current clients. Choose a number to specific details."
	bottom = ""
	
	location_choice = what_to_do(name_list, top, bottom, default_choice)
	os.system('clear')

	
	show_details(location_choice[1], locfile)


elif main_menu_choice[0] == main_menu.index('Run a pickup'):

	print '\n\nThis is going to run a pickup!'
	print '\n' * 10

	pickup_inputs = run_pickup('spike')

	add_to_csv(pickup_inputs)
	print '\n\n\n' * 3
	show_details(pickup_inputs['location'] , locfile )

	
	



	


