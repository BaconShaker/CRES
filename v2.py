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



# print "We are also going to need some packages..."
# for key in sys.modules():
# 	print key
# That will list the Imported Modules for you. 

# Now let's check which system is running 

if sys.platform.startswith('darwin'):
	print ""
	print "This is not a Linux, it's a Mac so you're going to get lost on the keyboard."
	print "It would be cool if you could actually specify if it's Robby or Mike too\n"

	locfile = os.path.expanduser( "~/Desktop/Python/location_list.csv" )  #mac
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

sheets = [ f for f in listdir(locfile) if isfile(join(locfile,f)) ]

print "Unsorted: ", sheets
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


class restaurant(object):
	def __init__(self, name, address, city, state, zip_code, contact_person, phone_num ):
		self.name = name
		self.address = address
		self.city = city
		self.state = state
		self.zip_code = zip_code
		self.contact_person = contact_person
		self.phone_num = phone_num

	# Make a function that shows the header(s) of the csv's

	# Going to need to read the names of the CSV's then add it to the Restaurant Object
	# Also going to need to opn each file to get the actual information to add it to the Object

	def add_restaurant(self):
		# Should probably check if the file exists already... I'll come back to this. 
		print sheets






























# Let us start the Program here, methinks
main_menu = [ 
	'List Restaurants',
	'Exit',
	]	

main1 = "This is a list of what this program can currently do:"
main2 = "Looking to add more now so hold tight... \n"
pick = what_to_do(main_menu, main1, main2, 0)

restaurant.add_restaurant(3)
