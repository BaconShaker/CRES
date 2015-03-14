#!/usr/bin/python


# This is the Menu script
from Tkinter import *
import ttk



class RouteBuilder():
	"""docstring for FrontPage"""
	def __init__(self, options):
		self.options = options
		self.alpha = []
		
		print "Options: This list is a placeholder for the locations list " ,  self.options
		
		# Need to make a menu, with a button and see how it returns from 
		# the loop when the window is closed... 


		def add_stop(nothing):
			x = lbox.curselection()
			if len(x)==1:
				idx = int(x[0])
	        	lbox.see(idx)
	        	print restaurant_names[idx]
	        	self.alpha.append( ( int( len(self.alpha) ),restaurant_names[idx] ) )

		page = Tk()
		page.title("Route Builder")
		mainframe = ttk.Frame(page, padding = " 3 3 12 12")
		mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
		mainframe.columnconfigure(0, weight=1)
		mainframe.rowconfigure(0, weight=1)

		

		# Build selectable field populated by the names of restatants
		restaurant_names = ('Argentina', 'Australia', 'Belgium', 'Brazil', 'Canada', 'China', 'Denmark', \
        'Finland', 'France', 'Greece', 'India', 'Italy', 'Japan', 'Mexico', 'Netherlands', 'Norway', 'Spain', \
        'Sweden', 'Switzerland')
		rnames = StringVar(value=restaurant_names)




		
		lbox = Listbox(mainframe, listvariable=rnames, height=5)
		

		
		# ttk.Button(mainframe, text = "Run Pickup", command = pickup ).grid(column = 2, row = 2)
		# ttk.Button(mainframe, text = "Add Stop", command = add_stop ).grid(column = 2, row = 3)
		# ttk.Button(mainframe, text = "List Locations", command = locations ).grid(column = 2, row = 4)

		# lbox = Listbox(mainframe, listvariable=rnames, height=5)
		ttk.Button(mainframe, text = "Add Stop", command = add_stop ).grid(column = 2, row = 3)


		lbox.grid(column=0, row=0, rowspan=6, sticky=(N,S,E,W))
		



		lbox.bind('<Double-1>', add_stop)
		
		page.mainloop()
		
		# The way this is working right now:
			# Makes a window that has buttons in it. Need to make your own buttons
			# in order to control the command each button runs.

			# When you hit a button, it runs the function called quit() below which
			# prints 'this is rob'

			# Each button should open a new window that can be used to do things like 
			# make a route, alter past submissions and check the price of YG.

			# Get to it! 
		
		
		
		# -------- FOR DEBUGGING --------
		

		print "\nalpha list [from end of display()]: " , self.alpha
		return the_end()

# -----------------------------------------------------------------


def the_end():
	print "\n\n\nThis is the end of the FrontPage loop. Whatever is placed here will be returned when the main window is closed"
	

# -----------------------------------------------------------------


def pickup():

	print "This is run pickup"

def locations():
	print "This is locations\n"
	




