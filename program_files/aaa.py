#!/usr/bin/python

# Here's what's currently in progress:
# 	Make the Tk() call happen in a function so it can return something
# 		or learn how to read class instances.


# This is the Menu script
from Tkinter import *
import ttk
import csv
from tabulate import tabulate


class Route():
	"""docstring for FrontPage"""
	def __init__(self, options, locfile):
		self.options = options
		self.route = []
		apple = open(locfile + '/master.csv')
		oranges = csv.DictReader(apple, dialect = 'excel', skipinitialspace = True)
		self.master_dict = oranges
		self.names = [x['Name'] for x in oranges]
		apple.close()

	def build(self):
		

		print self.names

		print "\nOptions: This list is a placeholder for the locations list " ,  self.options
		

		# Need to make a menu, with a button and see how it returns from 
		# the loop when the window is closed... 


		def add_stop(*args):
			x = lbox.curselection()
			if len(x) == 1:

				idx = int(x[0])
	        
	        	self.route.append( ( int( len(self.route) ), self.names[idx] ) )

	        	routebox.insert(len(self.route) - 1, self.names[idx] )
	        	routebox.update()
	        	r = self.names.pop(idx)

	        	self.rnames.set(value = tuple(self.names))

	        	# lbox.delete(idx)
	        	lbox.update()
	        
	        	for i in range(0,len(self.route),2):
					routebox.itemconfigure(i, background='#f0f0ff')

		def remove_stop():
			y = routebox.curselection()
			if len(y) == 1: 
				rem = int(y[0])
				self.names.append( ( int( len(self.names) ), self.route[rem] ) )

				o = self.route.pop(rem)
				self.rnames.set(value = tuple(self.names))
				

				lbox.insert(len(self.names) , self.route[idx] )

	        	lbox.update()
			print "Going to remove " , 

		def exit():
			page.destroy()

	        	



		# Set up the initial window and grid
		page = Tk()
		page.title("Route Builder")
		mainframe = ttk.Frame(page, padding = " 3 3 12 12")
		mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
		mainframe.columnconfigure(0, weight=1)
		mainframe.rowconfigure(0, weight=1)

		
		
		# Build selectable field populated by the names of restatants
		# restaurant_names = self.names

		# restaurant_names = ('Argentina', 'Australia', 'Belgium', 'Brazil', 'Canada', 'China', 'Denmark', \
  		#       'Finland', 'France', 'Greece', 'India', 'Italy', 'Japan', 'Mexico', 'Netherlands', 'Norway', 'Spain', \
 		#       'Sweden', 'Switzerland')

		self.rnames = StringVar()
		self.rnames.set(value = tuple(self.names))

		self.stops = StringVar()
		self.stops.set(value = tuple(self.route))
		

		# ttk.Button(mainframe, text = "Run Pickup", command = pickup ).grid(column = 2, row = 2)
		# ttk.Button(mainframe, text = "Add Stop", command = add_stop ).grid(column = 2, row = 3)
		# ttk.Button(mainframe, text = "List Locations", command = locations ).grid(column = 2, row = 4)


		# Create GUI elements here
		add_but = ttk.Button(mainframe, text = "Add Stop", command = add_stop)

		lbox = Listbox(mainframe, listvariable = self.rnames, height = 10)
		lbox.pack()

		routebox = Listbox(mainframe, listvariable = self.stops, height = 10)
		routebox.pack()

		quit = ttk.Button(mainframe, text = "Quit" , command = exit)

		# display = 


		# Set elements using .grid
		lbox.grid(column = 0, row = 0, rowspan = 6, sticky = (N,S,E,W) )
		add_but.grid(column = 2, row = 0)
		routebox.grid(column = 3, row = 0, rowspan = 6, sticky = (N,S,E,W) )
		quit.grid(column = 3, row = 8)


		# Set bindings
		lbox.bind('<Double-1>', add_stop)
		routebox.bind('<Double-1>', remove_stop)


		# Colorize alternating lines of the listbox
		for i in range(0,len(self.names),2):
			lbox.itemconfigure(i, background='#f0f0ff')
		
		page.mainloop()
		
		
		
		
		# -------- FOR DEBUGGING --------
		

		# print "\nalpha list [from end of display()]: " 
		# print tabulate( tuple(self.route) , headers = [" ", "Name"])
		# print "\n\n\n"
		# return the_end()  # Use this if you want to return something from OUTSIDE the class. Otherwise, 

		return self.route 

	def run():
		pass


# -----------------------------------------------------------------


def the_end():
	print "\n\n\nThis is the end of the RouteBuilder mainframe loop. Whatever is placed here will be returned when the main window is closed"


	

# -----------------------------------------------------------------


def pickup():

	print "This is run pickup"


	




