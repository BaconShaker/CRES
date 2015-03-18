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
		print oranges.fieldnames

		# Oranges is actually a list of dictionaries, each dictionary has the same keys. Each index is a new restaurant. 
		self.master_list = [dict(row) for row in oranges]
		# print self.master_list
		self.names = [just_names['Name'] for just_names in self.master_list]


		apple.close()
		


	def build(self):
		

		print self.names


		print "\nOptions: This list is a placeholder for the locations list " ,  self.options
		

		# Need to make a menu, with a button and see how it returns from 
		# the loop when the window is closed... 
	

		def add_stop(*args):
			

			
			sel = lbox.curselection()
			# Make sure you're only adding one place to the list at once to establilsh clear order. 
			print "Length of x" , len(sel)
			if len(sel) == 1:

				# idx is the integer index of the selected location to add in the listbox loop. 
				idx = int(sel[0])

				# matchmaker searches for the first occurence of the STRING (in the listbox box) returned by idx above 
				# 	to be compared against the master_list in order to add the correct address, regardless of order in the listbox.
				# 	Hopefully that allows of self.names to be Sorted before it's displayed by alphabeticle order. 
				matchmaker = [place['Name'] for place in self.master_list].index(self.names[idx])
	        	self.route.append(      (       int(len(self.route))   ,   self.names[idx]  , self.master_list[matchmaker]['Street Address'])           )

	        	# Add the selected restaurant to the routebox display. 
	        	routebox.insert(len(self.route) - 1, self.names[idx] )
	        	routebox.update()

	        	# Remove the selection from the choices listbox. 
	        	r = self.names.pop(idx)

	        	# Re.set() the StringVar()'s so the update() changes the display. 
	        	self.rnames.set(value = tuple(self.names))

	        	# lbox.delete(idx)
	        	lbox.update()

	        	# Make it so the rows' background alternates colors
	        	for i in range(0,len(self.route),2):
					routebox.itemconfigure(i, background='#f0f0ff')
				
			

					
		
		
				


		def remove_stop():
			# Essentially, this is the same as add route just in reverse. 
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
		lbox = Listbox(mainframe, listvariable = self.rnames, height = 10)
		lbox.pack()

		routebox = Listbox(mainframe, listvariable = self.stops, height = 10)
		routebox.pack()

		add_but = ttk.Button(mainframe, text = "Add Stop", command = add_stop )
		quit = ttk.Button(mainframe, text = "Close Window" , command = exit)
		remove_but = ttk.Button(mainframe, text = 'Remove Stop', command = remove_stop)

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
		print "This is: the_end(): " 
		print "\n\n\nThis is the end of the RouteBuilder mainframe loop. Whatever is placed here will be returned when the main window is closed"

		# checker = [ r[1] for r in self.route]
		# route_match = [ [ j['Name'], j['Street Address'] ] for j in self.master_list if j['Name'] in checker ]
		# for st in self.route:


		# print tabulate(route_match)

		print "This is the_end(), of Route."

		return self.route 

	def run():
		pass


# -----------------------------------------------------------------


def the_end():
	pass

	

# -----------------------------------------------------------------


def pickup():

	print "This is run pickup"


	




