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

def update_master(locfile, heads, in_dict2):
	fmaster = locfile + '/master2.csv'
	op = open(fmaster, 'wb')
	mast = csv.DictWriter(op, heads)
	mast.writeheader()
	print in_dict2
	for row in in_dict2:
		print row
		mast.writerow(row)
	op.close

def add_master(locfile, filename,  in_dict):
	fmaster = locfile + '/' + filename + '.csv'
	opt = open(fmaster, 'a')
	mast = csv.DictWriter(opt, in_dict.keys())
	# mast.writeheader()
	
	mast.writerow(in_dict)
	opt.close





class Keeper():
	"""docstring for ClassName"""
	def __init__(self, locfile):
		# Open master.csv and read the contents, store it for later use. 
		self.locfile = locfile
		apple = open(self.locfile + "/master2.csv")
		oranges = csv.DictReader(apple, dialect = 'excel', skipinitialspace = True)
		print "This is the list of fieldnames in the master.csv file, oranges[...] = " , oranges.fieldnames
		# Oranges is actually a list of dictionaries, each dictionary has the same keys. Each index is a new restaurant. 
		self.master_list = [dict(row) for row in oranges]
		apple.close()

		print "\n********************************\n"

	def master_lister(self):
		print "\nmaster_lister():\n"
		# Returns a list of dictionaries that are the rows in master.csv
		return self.master_list


	def all_names(self):
		# makes a list of all the names only and returns it
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
		# This doesn't work
		# It should add a scroll bar to the bottom of the show_master() screen
	        op, howMany = L[0], L[1]
	        if op == 'scroll':
	            units = L[2]
	            self.details.xview_scroll(howMany, units)
	        elif op == 'moveto':
	            self.details.xview_moveto(howMany)

	def show_master(self):
		# Displays the contents of master.csv 
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



	def make_donation():
		# Use this funciton to take money out of restaurant's accounts
		pass
		
	def collect_donation():
		# Use this to sum up the expected current (not paid out) donations
		pass



	def robby(self):
		for restaurant in self.master_list:
			print restaurant['Name']
			
	def write_master_csv(self):
		hea = self.master_list[0].keys()
		hea += ["Total Donation"]
		# hea.remove('Money To Charity')
		update_master(self.locfile, hea , self.master_list)
	# 	fmaster = self.locfile + '/master2.csv'
	# 	op = open(fmaster, 'wb')
	# 	mast = csv.DictWriter(op, self.master_list[0].keys())
	# 	mast.writeheader()
	# 	for row in self.master_list:
	# 		mast.writerow(row)
	# 	op.close

	def update_donation_total(self):
		# Returns a list of dictionaries, each dictionary is a single locaiton.file
		totals = {}
		for location in self.master_list:
			totals[location['Name']] = 0
			picker = open(self.locfile + '/' + location['Name'] + '.csv')
			reader = csv.DictReader(picker, dialect = 'excel', skipinitialspace = True)
			for collection in reader:
				print "------------------------\n"
				# print collection["Location"], collection['Expected Donation']
				totals[location['Name']] += float(collection['Expected Donation'])
				totals[location['Name']] = round(totals[location['Name']], 2)
		print "\nnew totals: ", totals

		for d in self.master_list:
			d['Money To Charity'] = totals[ d['Name'] ]
			
		update_master(self.locfile, self.master_list[0].keys()  ,self.master_list )
		self.pickup_keys = reader.fieldnames
		picker.close()

	def read_pickups():
		pass

	def add_client(self, to_add):
		add_master(self.locfile, "master2", to_add  )
		new_file = open(self.locfile + '/' + to_add['Name'] + ".csv", "wb")
		wri = csv.DictWriter(new_file, self.pickup_keys)
		wri.writeheader()
		new_file.close()




if __name__ == "__main__":
	locfile = os.path.expanduser( "~/GDrive/cres_sheets" ) 
	work = Keeper(locfile)
	# main.write_pickups_csv(collections_list)
	print "This is working!"
	work.robby()
	# work.write_master_csv()
	robster = {
		"robby" : "Is here", 
		"jason" : "Is at work"}
	work.update_donation_total()

	work.add_client()

