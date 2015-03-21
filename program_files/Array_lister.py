#!/usr/bin/python

from Tkinter import *
import ttk

# The Plan:
	# 	For BOTH display details as well as for input collection
	# 	__init__ all the dicts vars and such
	# 	write a def that displays them all 

root = Tk()
root.title("Collection Details")
mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

class Display_Array(object):

	def __init__(self, restaurants, *args):
		# restaurants needs to be a list of restarant names, to be used to get 
		# information later and to display. ORDER is important!!!
		self.restaurants = restaurants
	


	def turnmeon(self):
		root.mainloop()
		print "Fuck yeah!" , self.restaurants



robby = Display_Array(["1","2","3"])
robby.turnmeon()
