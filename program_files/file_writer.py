#!/usr/bin/python

# This is going to be the main writer class for 
# 	csv
# 	xlsx
# 	and many many more to come

collections_list = [ 
	{
		"Height (DEPARTURE): " 	: 21 ,
		"Pickup Score" 			: 34.38,
		"Collectable Material"  : 19.84,
		"Height (ARRIVAL): "    : 32,
		"Duration: "            : 0,
		"Service Fee"           : 0.15,
		"Gallons on Departure"  : 122.18,
		"Notes: "               : 0,
		"Donation Rate"         : 0.06,
		"Miles in Route"        : 7.5,
		"Stops on Route "       : 1,
		"Total Distance  "      : 7.5,
		'Date'                  : "2015-04-17 16:41:52.958848",
		'Fuel Surcharge'        : 2.465625,
		'Gallons on Arrival'	: 186.18,
		'Number of Stops' 		: 1,
		'Contact Person'		: 'Jibba Jabba',
		'Expected Revenue'		: 4.17,
		'Diesel Price'			: 2.63,
		'Oil Price'				: 0.21,
		'Contact Email'			: 'SomethingElse@gmail.com',
		'Gallons Collected'		: 64.0,
		'Expected Income'		: 2.976,
		'Quality (0 - 100): '	: 4,
		'Expected Donation'		: 1.1904,
		'Location'				:"Cobra Lounge",
	} ,
	{
		"Height (DEPARTURE): " 	: 43,
		"Pickup Score" 			: 34.38,
		"Collectable Material"  : 19.84,
		"Height (ARRIVAL): "    : 32,
		"Duration: "            : 0,
		"Service Fee"           : 0.15,
		"Gallons on Departure"  : 122.18,
		"Notes: "               : 0,
		"Donation Rate"         : 0.06,
		"Miles in Route"        : 7.5,
		"Stops on Route "       : 1,
		"Total Distance  "      : 7.5,
		'Date'                  : "2015-04-17 16:41:52.958848",
		'Fuel Surcharge'        : 2.465625,
		'Gallons on Arrival'	: 186.18,
		'Number of Stops' 		: 1,
		'Contact Person'		: 'Walkie Boogie',
		'Expected Revenue'		: 4.17,
		'Diesel Price'			: 2.63,
		'Oil Price'				: 0.21,
		'Contact Email'			: 'something@gmail.com',
		'Gallons Collected'		: 64.0,
		'Expected Income'		: 2.976,
		'Quality (0 - 100): '	: 4,
		'Expected Donation'		: 1.1904,
		'Location'				: "Mike's Place",
	} ]

# --------------------  --------------------------
# Height (DEPARTURE):   21
# Pickup Score          34.38
# Collectable Material  19.84
# Height (ARRIVAL):     32
# Duration:             0
# Service Fee           0.15
# Gallons on Departure  122.18
# Notes:                0
# Donation Rate         0.06
# Miles in Route        7.5
# Stops on Route        1
# Total Distance        7.5
# Date                  2015-04-17 16:41:52.958848
# Fuel Surcharge        2.465625
# Gallons on Arrival    186.18
# Number of Stops       1
# Contact Person        Robby Shintani
# Expected Revenue      4.17
# Diesel Price          2.63
# Oil Price             0.21
# Contact Email         rshintani@gmail.com
# Gallons Collected     64.0
# Expected Income       2.976
# Quality (0 - 100):    4
# Expected Donation     1.1904
# --------------------  --------------------------

import os.path #pathfinder
import time #this is for any delays I want
import sys
import os
from os import listdir
import csv
# from openpyxl import load_workbook
# from openpyxl import Workbook
from openpyxl import *
from Tkinter import *
import ttk
import tkFont



class Keeper():
	"""docstring for ClassName"""
	def __init__(self, locfile):
		
		self.locfile = locfile
		apple = open(self.locfile + "/master.csv")
		oranges = csv.DictReader(apple, dialect = 'excel', skipinitialspace = True)
		print "This is the list of fieldnames in the master.csv file, oranges[...] = " , oranges.fieldnames
		# Oranges is actually a list of dictionaries, each dictionary has the same keys. Each index is a new restaurant. 
		self.master_list = [dict(row) for row in oranges]
		apple.close()

	def master_lister(self):
		return self.master_list

	def all_names(self):

		print '\nStarting	all_names():'
		print "\n********************************\n"
		print "locfile:" , self.locfile
		
		# print self.master_list
		self.names = [just_names['Name'] for just_names in self.master_list]
		
		print "\n********************************\n"
		print "End of		all_names():"

		return self.names




	def write_pickups_csv(self, collections_list):
		# This funciton takes the usr_inputs in main_program.py and adds them
		# 	to their respective .csv file. 

		# If you change the fieldnames however, it WILL ERASE THE ENTIRE FILE 
		# 	and re write over with the same name.


		print '\nStarting	write_pickups_csv():'
		print "\n********************************\n"
		print collections_list[0].keys() , '\n'
		for collection in collections_list:
			target = self.locfile + "/" + collection['Location'] + '.csv'
			r = open(target)
			fdr = csv.DictReader(r, dialect = 'excel', skipinitialspace = True)
			pickup_count = 1
			for line in fdr:
				pickup_count += 1 
			print "This is pickup #:" , pickup_count
			collection['pickup_count'] = pickup_count
			howlong_add = len(collection.keys())
			howlong_fdr = len(fdr.fieldnames) 
			print "fdr: " , howlong_fdr
			print "to_add: " , howlong_add 
			if howlong_fdr == howlong_add:
				# This one only writes the INPUT ROW.
				fw = open(target, 'a')	
				writer = csv.DictWriter(fw, collection.keys())
				writer.writerow(collection)
				fw.close()
			else:
				# This overwrites the file completely, may be a good idea to make a script here that 
				# moves the file that's being replaced to a safe location?
				fw = open(target, 'wb')	
				writer = csv.DictWriter(fw, collection.keys())
				writer.writeheader()
				writer.writerow(collection)
				fw.close()
			r.close()
		print "\n********************************\n"
		print "End of		write_pickups_csv():"


	def __scrollHandler(self, *L):
	        op, howMany = L[0], L[1]

	        if op == 'scroll':
	            units = L[2]
	            self.details.xview_scroll(howMany, units)
	        elif op == 'moveto':
	            self.details.xview_moveto(howMany)

	def show_master(self):
		print ""

		# Need to set up the details Frame
		page = Tk()
		page.title("Master File")
		self.details = ttk.Frame(page, padding = " 3 3 12 12")
		self.details.grid(column = 0, row = 0, sticky = (N, W, E, S))
		# scroll = ttk.Scrollbar(self.details, orient= 'horizontal', command=self.__scrollHandler).grid(row=50, columnspan = len(self.master_list[0]), sticky= E+W)
		# print self.details
		# s = ttk.Scrollbar( page, orient="horizontal" , command=self.details.xview)
		# page.configure(xscrollcommand=s.set)
		# details.columnconfigure(0, weight = 1)
		# details.rowconfigure(0, weight = 1)
		row = 0
		col = 0
		for key in self.master_list[0]:
			print key
			head = ttk.Label(self.details, text = key, font = 'bold').grid(row = 0, column = 2 * col) 

			# head.configure(hunderline = True)
			col += 1
			
		rob = 0
		for place in self.master_list:
			row += 1
			rob = 0
			for loc in place:
				self.entry = ttk.Label(self.details, text = place[loc]).grid(row = row, column = 2 * rob )
				ttk.Separator().grid(row = row , column = 2 * rob + 1)
				rob += 1 
			
		self.details.mainloop()
		print "That's all folks!"




	def loaditup(self):
		print "\nStarting	loaditup():"
		print '\n********************************\n'
		master = load_workbook(self.locfile + '/mordor.xlsx')
		self.master = master
		print master.get_sheet_names()
		print "\n********************************\n"
		print "End of		loaditup():"


	def checks_worksheet(self, temp_dict):
		print "\nStarting	check_worksheet():"
		print '\n********************************\n'
		if "All Pickups" in self.master.get_sheet_names():
			print "All Pickups is a worksheet!"
			print ""
			
		else:
			pickup_sheet = self.master.create_sheet(1)
			pickup_sheet.title = "All Pickups"
			pickup_sheet.append(temp_dict.keys())
			print "Header row added to All Pickups:", temp_dict.keys()
			self.master.save(self.locfile + '/mordor.xlsx')
			
		print "\n********************************\n"
		print "End of		check_worksheet():"


	def write_collections(self, collections_list):
		print "\nStarting	write_collections():"
		print '\n********************************\n'
		# for collection in collections:
		# 	print "------------------- "
		# 	for key in collection:
		# 		print key , ":	" , collection[key]

		# Check the headers on the master pickups file
		pickups = self.master.get_sheet_by_name('All Pickups')
		for col in range( 1, len(collections_list[1] ) + 1 ):
			print pickups.cell(row = 1 , column = col).value()

		# for collection in collections_list:
			# pickups.append(collection)



		print "\n********************************\n"
		print "End of		write_collections():"
	

	def read_pickups():
		pass

	def new_client():
		pass



if __name__ == "__main__":
	locfile = os.path.expanduser( "~/GDrive/cres_sheets" ) 
	main = Keeper(locfile)
	
	# main.write_pickups_csv(collections_list)
	print "This is working!"
	main.show_master()


	# main.loaditup()
	# main.checks_worksheet(collections_list[1])
	# main.write_collections(collections_list)



