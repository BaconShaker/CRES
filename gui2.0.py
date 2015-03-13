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

		for i, but in enumerate(options):
			ttk.Button(mainframe, text = but, command = quit).grid(column = 1, row = len(options) + i)
		
		# The way this is working right now:
			# Makes a window that has buttons in it. The words on the buttons are
			# input from menu_options. 

			# When you hit a button, it runs the function called quit() below which
			# prints 'this is rob'

			# Each button should open a new window that can be used to do things like 
			# make a route, alter past submissions and check the price of YG.

			# Get to it! 


		page.mainloop()




	def function():
		pass
		

# -----------------------------------------------------------------


def quit():

	print "This is rob"

menu_options = ['quit', 'Build Route' ,'Run Pickup']


main = FrontPage(menu_options)








