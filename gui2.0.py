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

class FrontPage():
	"""docstring for FrontPage"""
	def __init__(self, options):
		self.options = options
		
		print "Options: " ,  self.options

		# Need to make a menu, with a button and see how it returns from 
		# the loop when the window is closed... 

		page = Tk()
		page.title("Main Menu")
		mainframe = ttk.Frame(page, padding = " 3 3 12 12")
		mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
		mainframe.columnconfigure(0, weight=1)
		mainframe.rowconfigure(0, weight=1)

		
		ttk.Button(mainframe, text = "Run Pickup", command = pickup ).grid(column = 1, row = 2)
		ttk.Button(mainframe, text = "Route Builder", command = alpha.append(robby.blab()) ).grid(column = 1, row = 3)
		ttk.Button(mainframe, text = "List Locations", command = locations ).grid(column = 1, row = 4)
		
		
		# The way this is working right now:
			# Makes a window that has buttons in it. Need to make your own buttons
			# in order to control the command each button runs.

			# When you hit a button, it runs the function called quit() below which
			# prints 'this is rob'

			# Each button should open a new window that can be used to do things like 
			# make a route, alter past submissions and check the price of YG.

			# Get to it! 


		page.mainloop()
		print "This is alpha" , 

		return the_end()

# -----------------------------------------------------------------


def the_end():
	print "\n\n\nThis is the end of the FrontPage loop. Whatever is placed here will be returned when the main window is closed"
	

# -----------------------------------------------------------------


def pickup():

	print "This is run pickup"

def locations():
	print "This is locations"






class Collection():
	"""docstring for ClassName"""
	def __init__(self):
		
		self.count = 0
		print "This is a Collection"

	def blab(self):

		print "This is a collection function "
		self.count += 1
		return "This is the answer #", self.count
		

menu_options = ['quit', 'Build Route' ,'Run Pickup']


# When you hit the button with the robby.blab command, it runs correctly. 
col = 0 
robby = Collection()


alpha = []
main = FrontPage(menu_options)

print "ALPHA2:" , alpha

# rob = robby.blab()
# print rob











