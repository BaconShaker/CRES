#!/usr/bin/python

# This should make a class to run pickups at each location.... Should. 

# Cheating...

from tabulate import tabulate #makes the nice tables
import os.path #pathfinder
import time #this is for any delays I want
import sys
import os
from os import listdir
import csv
import urllib
import urllib2
from bs4 import BeautifulSoup		# pip install BeautifulSoup4




# First let's check which system is running.
	# Need to find a way to get the GDrive file on the the Linux side of things. That's going to be hard

# -----------------------------------------------------------------

if sys.platform.startswith('darwin'):
	print ""
	print "This is not a Linux, it's a Mac so you're going to get lost on the keyboard."
	print "It would be cool if you could actually specify if it's Robby or Mike too\n"

	locfile = os.path.expanduser( "~/GDrive/cres_sheets" )  #mac
	print "Locfile: ", locfile, '\n'
	sheets = [ f for f in listdir(locfile)   ]
	sheets.remove('.DS_Store') # Not sure what this is but we don't want it.

elif sys.platform.startswith('linux'):
	print ""
	print 'This is a Linux\n' 
	locfile = os.path.expanduser( '~/cres_sheets2')
	print "Locfile: ", locfile, '\n'
	sheets = [ f for f in listdir(locfile)   ]


# -----------------------------------------------------------------


class Menu_main():
	def __init__(self, prefix , choices, suffix, default,  *args):

		print "\nMenu usage: Name(string, list, string, int)"
		# Here's all the attributes the menu is going to have upon initialization. Can add more later
		self.prefix = prefix
		self.choices = choices # May have to do some [choice.decode('utf-8') for choice in choices]
		self.suffix = suffix
		self.default = default

	def display(self):
		os.system('clear')
		print '\n' , '	', self.prefix , '\n'
		trunk_list = [ ( '		' + str(index ) , choice ) for index, choice in enumerate(self.choices) ]
		print tabulate( trunk_list , tablefmt ='plain')  
		print '\n' , '			', self.suffix ,'\n' , '						[BLANK] --> ' , self.default

		# Got the table to display ok but now I need to get the rawinput to return the same things as in v2.py
		# Should be in the format of:  
		#								response = [ int(selection), word] 
		# 	This should be ok now. 

		selection = raw_input()
		# while selection not in trunk... ? I don't think I need this bc it should loop outside this fcn
			
		if selection == '':
			selection = self.default

		else:
			selection = selection 
			# Not sure I neeeeeeed this, but something tells me it's a good idera to keep it here for the time being. 
			# Can figure it out later, eh?
			# Need to figure out how to get word and 

		try: 
			word = self.choices[ int(selection) ]
		except IndexError:
			print "You picked something not on the list"
			word = 'Try harder'
		# print 'Good work, you picked: ' , selection
		# print 'Hopefully your choice was: ' , word
		response = [ int (selection) , word ]

		print "\nResponse: " , response 
		return response

	def return_to_main(self):
		return 0


# -----------------------------------------------------------------

def make_locations(locfile):

	# Here is the list that controls the headers on the pickup_files
	pickup_heads = []

	# Open the master file and get the nicknames. The Nicknames will become the individual
	# filenames for the pickup files. 

	apple = open(locfile + '/master.csv')
	oranges = csv.DictReader(apple, dialect = 'excel', skipinitialspace = True)

	nicknames = [x['Name'] for x in oranges]
	print "Files exist for: " 
	for nick in nicknames:
		pickup_file = locfile + '/' + nick + '.csv'
		if os.path.exists(pickup_file):
			print  '		', nick 
			

		else:
			print "There is no '" ,  pickup_file   , "' we should make one!\n" 
			to_make = open( pickup_file, 'a' )
			writer = csv.DictWriter( to_make , fieldnames = pickup_heads)
			writer.writeheader()
			to_make.close() 
	return nicknames
	apple.close()

# -----------------------------------------------------------------


from Tkinter import *
import ttk
from datetime import date

class Collection():
	def __init__(self):
		print "this can be use as a function?"
		self.link_diesel = 'http://www.eia.gov/dnav/pet/pet_pri_gnd_dcus_r20_w.htm'
		self.link_ams = 'http://www.ams.usda.gov/mnreports/nw_ls442.txt'

		
		# Need to get work on this parser.  

		print ""
		print "Price_lookup():" # Input gallons or inches?
		print ""
		response = urllib2.urlopen(self.link_ams)
		# response = urllib2.urlopen('http://www.ams.usda.gov/mnreports/nw_ls442.txt')
		soup = BeautifulSoup(response)
		
		# page = response.readline()
		text = soup.get_text()
		self.yg_price = text[text.index('Choice white') :text.index('EDBLE LARD')]
		print text
		print ""
		ams_edit = text[text.index('Des') : text.index('2015') + 4 ].replace("     ", "\n Current as of ")
		self.ams_location = ams_edit



	# Should add the ability to build the route just before making inputs Below
	# that way you'll have the distance for the fuel calculation. Once you make the list 
	# you should be able to iterate through the list to make inputs




	def main_prompt(self):

		def price_lookup():
			print "Price Lookup window should have just popped open.\n"
			# Get AMS price
			# This is going to pop open its own window
			lookup = Tk()
			lookup.title("AMS Price Lookup")
			subframe = ttk.Frame(lookup, padding = " 3 3 12 12")
			subframe.grid(column=0, row=0, sticky=(N, W, E, S))
			subframe.columnconfigure(0, weight=1)
			subframe.rowconfigure(0, weight=1)
			ttk.Label(subframe, text = "AMS Report from: " + self.ams_location).grid(column = 0, row = 0)
			ttk.Label(subframe, text = " ----------------------------------------").grid(column = 0, row = 1)
			ttk.Label(subframe, text = self.yg_price).grid(column = 0, row = 2)
			lookup.mainloop()
			

		def today():
			print date.today()
			date_of_pickup.set(date.today())

		def grab_inputs():
			to_return = [variable.get() for variable in answers]
			to_return.insert(0, loc_select.get() )
			print to_return
			






		root = Tk()
		root.title("Collection Details")

		mainframe = ttk.Frame(root, padding="3 3 12 12")
		mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
		mainframe.columnconfigure(0, weight=1)
		mainframe.rowconfigure(0, weight=1)

		# set up the variables, these should match what's in the answers list
		arrive = StringVar()
		depart = StringVar()
		duration = StringVar()
		qual = StringVar()
		volume = StringVar()
		date_of_pickup = StringVar()
		stop_number = StringVar()
		price = StringVar()
		

		loc_select = StringVar()
		# Need to add variables like this:
			# trying = StringVar()

		questions = [
			# "Add a VARIABLE string Here" ,
			'Date (pickup): ' ,
			'Arrivial (in):' ,
			'Departure (in):' ,
			"Price (cwt):" ,
			"Duration (hrs)" , 
			"Quality (0-100)", 
			# "Stop #: " ,
		]

		answers = [ 
			# add_variable ,
			date_of_pickup , 
			arrive , 
			depart , 
			price ,
			duration , 
			qual,
			# stop_number ,
		]


		# This is the setup for the drop down menu for location selection
		choices = ['Choose Location']
		for name in name_list:
			choices.append(name)
		print name_list
		ttk.OptionMenu(mainframe, loc_select, *choices).grid(column = 1,  row = 0, sticky = W)
		
		# Display stop number
		ttk.Label(mainframe, text = "Stop #: " , ).grid(column = 1, row = 1)
		ttk.Label(mainframe, textvariable = stop_number).grid(column = 2, row = 1)

		# This builds the input prompts from the lists questions and answers above
		start_on = 2
		for i , q in enumerate(questions):
			ttk.Label(mainframe, text = q).grid(column = 1, row = i + start_on)
			ttk.Entry(mainframe, textvariable = answers[i] ).grid(column = 2, row = i + start_on)

		# Make a button to enter today's date quickly
		ttk.Button(mainframe, text = 'Enter TODAY' , command = today).grid(column = 3, row = questions.index('Date (pickup): ') + 2 )

		# Put a button look up the AMS Price
		ttk.Button(mainframe, text = 'AMS Price Lookup', command = price_lookup).grid(column = 3, row = questions.index('Price (cwt):') + 2)

		# Make a button that submits what's in the fields
		submit = ttk.Button(mainframe, text = 'Submit', command = grab_inputs).grid(column = 3, row = len(choices) + 2)

		# ttk.Label(mainframe, text = "-------------------------------").grid(column = 0, row = len(choices) + 3 )
		ttk.Label(mainframe, text = "-------------------------------").grid(column = 1, row = len(choices) + 3)
		ttk.Label(mainframe, text = "-------------------------------").grid(column = 2, row = len(choices) + 3)
		ttk.Label(mainframe, text = "-------------------------------").grid(column = 3, row = len(choices) + 3)

		for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)


		# root.bind('<Return>', inches_to_gallons)
		# root.bind('<Return>', calculate)

		
		root.mainloop()
		print "\n\nqual: " , qual.get()
		final = [
			ans.get() for ans in answers
		]
		final.insert( 0 , loc_select.get())
		return list(final)



	def conversions(self):
		print "This is working!!!"
		

		# This should be on top so it can be called later. 


	def arrival(self):
		print "This is the on arrival def"
		print self.link_diesel
		# Need to get Location, initial height, condition of bin(?), record/input time, 
		# Do math 


	def weather(self):
		print "This def should get the local weather conditions"
		# Would be a nice spot for some geocoding, CDMA hackathonage. 
















# ----------------------------------------------------------------------------

	# This is the beginning of the actual "program" I think the menu
	# function is working ok. Time to move on to adding the other options



pre = 'This is the Main Menu, by all means choose an option:'
post = 'Thanks, jackass... '
main_choices = ['EXIT PROGRAM', 'Run Pickup', 'choice 2', "yadda y'adda yadda"]

# Load the Menu to a variable, 
main_menu = Menu_main(pre, main_choices, post, 1)




# Start the main loop. 
to_loop = 1
while to_loop != 0:
	# This is the main list of locations, got it from master.csv
	name_list = make_locations(locfile)
	# First prompt of Main Menu
	menu_choice = main_menu.display()
	print menu_choice

	# Below are all the programs associated with the choices in main_menu

	# First, let's let ourselves out of the loop. 
	if menu_choice[0] == main_choices.index('EXIT PROGRAM'): 
		break










# Here is where I'm working on the plane. 

	elif menu_choice[0] == main_choices.index('Run Pickup'):
		print "Run a pickup"

		# Define a Collection variable to get the ball rolling
		collect = Collection()
		pickup = collect.main_prompt()
		print '\nYou chose to run a pickup, here are the results: ' , pickup





	elif menu_choice[0] == main_choices.index('choice 2'):
		print "That worked I think"

	else:
		os.system('clear')
		print "\n" * 7
		print "Nigga, '" , menu_choice[0] , "' wasn't a choice! Go fish! \n(Or that choice is not functiong just yet)"
		time.sleep(2)







	# This will end the main while loop
	# to_loop = main_menu.exit()


