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
		print before
		print ""
		count = 0
		counter = [0,]
		for choice in choices:
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
			word = word.replace("\xe2\x80\x99" , "'")
			response = [ int(selection), word] 
			return response
			looper = looper + 1

# -----------------------------------------------------------------

class Restaurant(object):
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
	pickup_heads = [ 'Date' , 'Collected' ]

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
			writer = csv.DictWriter(to_make, fieldnames = pickup_heads )
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

def display_names(master_dir):
	names = []
	with open(master_dir + '/master.csv') as fp:
		reader = csv.DictReader(fp, dialect = 'excel', skipinitialspace = True)

		# for row in reader:

	return names


















# Let us start the Program here, methinks
# Load the restaurants into the class. 
name_list = make_locations(locfile)


# robby = class_loader(locfile)
# print robby['Erie Cafe']['536 W. Erie Street']



main_menu = [ 
	'List Restaurants',
	'Exit',
	]	

main1 = "This is a list of what this program can currently do:"
main2 = "Looking to add more now so hold tight... \n"
pick = what_to_do(main_menu, main1, main2, 0)


# re if pick below, 
# 	[0] is the number input from the prompt,
# 	[1] should be the string in 'word' from the list 


if pick[0] == 0:
	print name_list
elif pick == 1:
	pass


