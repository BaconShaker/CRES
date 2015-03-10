#!/usr/bin/python

# This should make a class to run pickups at each location.... Should. 

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
		from Tkinter import *
		import ttk
		from datetime import date

	except ImportError as err:
		print "Something didn't work right.\n"
		print  err.args

	mods = 0


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



# -----------------------------------------------------------------


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

		def finalize():
			to_return = [variable.get() for variable in answers]
			to_return.insert(0, loc_select.get() )
			
			ttk.Label(mainframe, text = "Close the window to add: \n").grid(column = 1, row = len(choices) + 4)
			
			# print "\n\nConversions from finalize: \n 			" , self.conversions(to_return)

			check_final = self.conversions(to_return)
			for index, key in enumerate(check_final):
				ttk.Label(mainframe, text = key.replace( '_' , " " ) ).grid(column = 2, row =  index + len(choices) + 5, sticky = E)
				ttk.Label(mainframe, text = check_final[key] ).grid(column = 3, row =  index + len(choices) + 5, sticky = N )

			

			return to_return


		root = Tk()
		root.title("Collection Details")

		mainframe = ttk.Frame(root, padding="3 3 12 12")
		mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
		mainframe.columnconfigure(0, weight=1)
		mainframe.rowconfigure(0, weight=1)

		# set up the variables, these should match what's in the answers list
		arrive = IntVar()
		depart = IntVar()
		duration = IntVar()
		qual = IntVar()
		volume = DoubleVar()
		date_of_pickup = StringVar()
		stop_number = IntVar()
		price = DoubleVar()
		cres_fee = DoubleVar()

		
		robby = StringVar()
		loc_select = StringVar()

		# Making the defaults
		arrive.set(30)
		depart.set(1)
		price.set(23.0)
		qual.set(50)
		cres_fee.set(.15)
		
		date_of_pickup.set("2015-MM-DD")
		# Need to add variables like this:
			# trying = StringVar()

		questions = [
			# "Add a VARIABLE string Here" ,
			'Date (pickup): ' ,
			'Arrivial (in):' ,
			'Departure (in):' ,
			"Price (cwt):" ,
			"Duration (hrs):" , 
			"Quality (0-100):", 
			"Fee ($/lb):",
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
			cres_fee, 
			# stop_number ,
		]


		# This is the setup for the drop down menu for location selection
		choices = ['Choose Location']
		for name in name_list:
			choices.append(name)
		print "\nname_list" , name_list
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
		ttk.Button(mainframe, text = 'Finalize', command = finalize).grid(column = 2, row = len(choices) + 2)
		# ttk.Button(mainframe, text = 'PUSH', command = )

		# ttk.Label(mainframe, text = "-------------------------------").grid(column = 0, row = len(choices) + 3 )
		ttk.Label(mainframe, text = "-------------------------------").grid(column = 1, row = len(choices) + 3)
		ttk.Label(mainframe, text = "-------------------------------").grid(column = 2, row = len(choices) + 3)
		ttk.Label(mainframe, text = "-------------------------------").grid(column = 3, row = len(choices) + 3)

		for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)


		# root.bind('<Return>', inches_to_gallons)
		# root.bind('<Return>', calculate)

		# Opens the INPUT Screen
		root.mainloop()


		
		# Build the output, need to .insert() any additional variables that aren't in answers
		final = [
			ans.get() for ans in answers
		]
		final.insert( 0 , loc_select.get())
		print "Here's what's going into conversions(): " , final

		return list(final)



	def conversions(self, *input_data):
		# print "input data: " , input_data
		# input_data is in the form :
		# 								0Location name
		# 								1date
		# 								2arrival inches
		# 								3depart inches 
		# 								4price (cwt)
		# 								5durarion (hrs)
		# 								6quality (whole number)
		#								7service_fee
		# 								7pickupcount?
		# 								7(not yet) route info

		# First let's convert inches cubed to gallons
		# Total volume:
		h = 36
		w = 28
		l = 48

		# Measured heights:
		a_height = input_data[0][2]
		d_height = input_data[0][3]

		a_vol = float( l * w * a_height) * 0.0043290
		d_vol = float(l * w * d_height) * 0.0043290

		# x_vol is in GALLONS! ( multiplied by 0.0043290 )

		# Convert gallons to lbs
		lbs_per_gallon = 7.75 #/gal
		a_lbs = a_vol * lbs_per_gallon 
		d_lbs = d_vol * lbs_per_gallon

		gal_collected = a_vol - d_vol
		lbs_collected = a_lbs - d_lbs

		price = input_data[0][4] / 100.0

		service_fee = input_data[0][7]


		inputs = {
			"Gallons_Collected" : round(gal_collected, 2) ,
			"Pounds_Collected" : round(lbs_collected, 2) ,
			"Fuel_Price" : price, 
			"Score" : round(lbs_collected / a_lbs , 2) * 100 ,
			"Location" : input_data[0][0] , 
			"Total_Income" : round(price * lbs_collected, 2) ,
			"To_CRES" : round((service_fee) * lbs_collected , 2) ,
			"To_Charity" : round((price - service_fee) * lbs_collected , 2), 
			"Date_of_Pickup" : input_data[0][1],
			"Left_Behind" : round(d_vol,2),
			"Duration" : input_data[0][5],
			"Arrivial_Height" : input_data[0][2],
			"Departure_Height" : input_data[0][3],
		}

		# print "inputs from conversions:"
		# for key in inputs:
		# 	print "				" , key , ":", inputs[key]


		# robby.set('0')
		self.inputs = inputs
		return inputs
		

		
	def write_to_csv(self, writer):
		print "This def should get the local weather conditions"
		
		
		# Would be a nice spot for some geocoding, CDMA hackathonage. 




class Clients():
	def __init__(self):
		apple = open(locfile + '/master.csv')
		oranges = csv.DictReader(apple, dialect = 'excel', skipinitialspace = True)
		self.master_dict = oranges
		self.names = [x['Name'] for x in oranges]

	def make_locations(self, locfile):


		# Here is the list that controls the headers on the pickup_files
		pickup_heads = []

		# Open the master file and get the nicknames. The Nicknames will become the individual
		# filenames for the pickup files. 

		print self.master_dict.fieldnames

		

		for nick in self.names:
			pickup_file = locfile + '/' + nick + '.csv'
			if os.path.exists(pickup_file):
				print "YAY! There's a file for: " , nick

			else:
				print "There is no '" ,  pickup_file   , "' we should make one!\n" 
				to_make = open( pickup_file, 'a' )
				writer = csv.DictWriter( to_make , fieldnames = pickup_heads)
				writer.writeheader()
				to_make.close() 
		
	



	def show_details(self, location, locfile):
		os.system('clear')
		
		fo = open(locfile + '/' + location + '.csv' )
		fr = csv.DictReader(fo, dialect = 'excel', skipinitialspace = True)
		print fr.fieldnames
		# heads = fr.fieldnames
		# print fr.iteritems
		new_fr = []
		print ""
		count = 0
		to_show = [  ]
		for row in fr:
			new_fr.append( { key.replace( '_' , ' ') : value for key, value in row.items() if key in to_show} )
	 		count += 1
		# print '\n' * 10
		# print 'New fr: ' , new_fr
		print "These are the stats for" , location , ':\n\n' 
		# print "new_fr: " , new_fr
		print tabulate(new_fr, headers = 'keys') , '\n\n\n\n'

		print 'Press [ENTER] key to continue...\n'
		pause = raw_input()

		return tabulate(new_fr, headers = 'keys') , '\n\n\n\n'

		fo.close()











# ----------------------------------------------------------------------------

	# This is the beginning of the actual "program" I think the menu
	# function is working ok. Time to move on to adding the other options



pre = 'This is the Main Menu, by all means choose an option:'
post = 'Thanks, jackass... '
main_choices = ['EXIT PROGRAM', 'Run Pickup GUI', 'Run Pickup txt' , 'Client List', "yadda y'adda yadda"]

# Load the Menu to a variable, 
main_menu = Menu_main(pre, main_choices, post, 1)
collect = Collection()
places = Clients()
places.make_locations(locfile)


# Start the main loop. 
to_loop = 1
while to_loop != 0:
	# This is the main list of locations, got it from master.csv

	name_list = places.names
	# First prompt of Main Menu
	menu_choice = main_menu.display()
	print menu_choice

	# Below are all the programs associated with the choices in main_menu

	# First, let's let ourselves out of the loop. 
	if menu_choice[0] == main_choices.index('EXIT PROGRAM'): 
		break


	elif menu_choice[0] == main_choices.index('Run Pickup GUI'):
		print "Run a pickup"

		# Define a Collection variable to get the ball rolling
		
		pickup = collect.main_prompt()
		
		collection_inputs = collect.conversions(pickup)
		print '\nYou chose to run a pickup, here are the results:\n ' 
		print tabulate( [ (key, collection_inputs[key] ) for key in collection_inputs] )
		print '\n'

		collect.write_to_csv(collection_inputs)

	elif menu_choice[0] == main_choices.index('Run Pickup txt'):
		print "This is where the plug and chug method should go"
		time.sleep(2)

	elif menu_choice[0] == main_choices.index('Client List'):
		print "That worked I think"
		alpha = "Here's a list of our Clients,"
		beta = "Choose one to see more details!"
		

		p = Menu_main(alpha, name_list, beta, 1)
		q = p.display()

		place.show_details( q[1] , locfile )


	else:
		os.system('clear')
		print "\n" * 7
		print "Nigga, '" , menu_choice[0] , "' wasn't a choice! Go fish! \n(Or that choice is not functiong just yet)"
		time.sleep(2)







	# This will end the main while loop
	# to_loop = main_menu.exit()


