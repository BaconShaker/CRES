#!/usr/bin/python


# This is the Menu script
from Tkinter import *
import ttk
from aaa import Robby


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
		ttk.Button(mainframe, text = "Route Builder", command = build_route ).grid(column = 1, row = 3)
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
		return the_end()
		

		# return alpha

# -----------------------------------------------------------------


def the_end():
	print "\n\n\nThis is the end of the FrontPage loop. Whatever is placed here will be returned when the main window is closed"
	

# -----------------------------------------------------------------


def pickup():

	print "This is run pickup"

def locations():
	print "This is locations"



def build_route():
	print "This is where you'll build a route"
