#!/usr/bin/python

# This should make a class to run pickups at each location.... Should. 

# Cheating...

from tabulate import tabulate #makes the nice tables
import os.path #pathfinder
import time #this is for any delays I want




class Menu():
	def __init__(self, prefix , choices, suffix, default,  *args):
		if default == 0:
			print "Sorry but your default choice is not imaginary. Try again and don't use 0."
		print "Usage: Name(string, list, string, int)"
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

		word = self.choices[ int(selection) ]
		# print 'Good work, you picked: ' , selection
		# print 'Hopefully your choice was: ' , word
		response = [ int (selection) , word ]

		print "\nResponse: " , response 
		return response

	def return_to_main(self):
		return 0












class Collection():
	def __init__(self):
		print "this can be use as a function?"
		self.link_diesel = 'http://www.eia.gov/dnav/pet/pet_pri_gnd_dcus_r20_w.htm'
		self.link_ams = 'http://www.ams.usda.gov/mnreports/nw_ls442.txt'

	def conversions(self):
		pass

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

# Define a Collection variable to get the ball rolling
pickup = Collection()
print "\n"

# Get arrivial stats:
pickup.arrival()

















# This is the beginning of the actual "program" I think the menu
# function is working ok. Time to move on to adding the other options



pre = 'This is the Main Menu, by all means choose an option:'
post = 'Thanks, jackass... '
main_choices = ['EXIT PROGRAM', 'choice 1', 'choice 2', "yadda y'adda yadda"]

# Load the Menu to a variable, 
main_menu = Menu(pre, main_choices, post, 1)

# Actually do things with the Menu, like display it. 
# main_menu.display()





# This is the main loop. 
to_loop = 1
while to_loop != 0:

	# First prompt of Main Menu
	menu_choice = main_menu.display()
	print menu_choice

	# Below are all the programs associated with the choices in main_menu

	# First, let's let ourselves out of the loop. 
	if menu_choice[0] == main_choices.index('EXIT PROGRAM'): 
		break

	elif menu_choice[0] == main_choices.index('choice 2'):
		print "That worked I think"

	elif menu_choice[0] == main_choices.index('choice 1'):
		print "This is choice 2!"

	else:
		os.system('clear')
		print "\n" * 7
		print "Nigga, that wasn't a choice! Go fish! \n(Or that choice is not functiong just yet)"
		time.sleep(2)







	# This will end the main while loop
	# to_loop = main_menu.exit()


