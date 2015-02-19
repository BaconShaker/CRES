#!/usr/bin/python

# This should make a class to run pickups at each location.... Should. 

# Cheating...

from tabulate import tabulate
import os.path



class Menu():
	def __init__(self, prefix , choices, suffix, default,  *args):
		print 'I hope this takes lists?'
		print "Usage: Name(string, list, string, int)"
		self.prefix = prefix
		self.choices = choices
		self.suffix = suffix
		self.default = default

	def display(self):
		os.system('clear')
		print '\n' , '	', self.prefix , '\n'
		print tabulate( [ ( '		' + str(index + 1) , choice ) for index, choice in enumerate(self.choices) ] , tablefmt ='plain')  
		print '\n' , '			', self.suffix ,'\n' , '						[BLANK] --> ' , self.default

		# Got the table to sidplay ok but now I need to get the rawinput to return the same things as in v2.py
		# Should be in the format of:  
		#								response = [ int(selection), word] 



















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


















pre = 'This is the Main Menu, by all means choose an option:'
post = 'Thanks, jackass... '
questions = ['choice 1', 'choice 2', 'yadda yadda yadda']

# Load the Menu to a variable, 
main_menu = Menu(pre, questions, post, 0)

# Actually do things with the Menu, like display it. 
main_menu.display()

