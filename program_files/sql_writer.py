#!/Applications/MAMP/Library/bin/python

# This file should write the user inputs from routebuilder in a MySQL database
# instead of in a csv file

import mysql.connector


loc = {
	"Name" : "Jabba Walkie Boogie Time",
	"Address" : "1224 Chicago Ave",
	"Zip" : 60611,
	"City" : "Chicago",
	"Email" : "renewable@gmail.com",
	"Contact": "Roby",
	"Phone Number" : 1234567890,
	"Last Pickup" : '2015-05-01',
	"Next Pickup" : '2015-05-02', 
	"Charity" : "Friends of Whitney Young", 
	"Notes" : "This is a new place, ok to delete",
}

print "hello"
config = {
	  'user': 'robby',
	  'password': 'cres1234',
	  'host': 'localhost',
	  'database': 'CRES',
	  'raise_on_warnings': True,
	  'port': 8888
	}





db = mysql.connector.connect(**config)
cursor = db.cursor()



class Sql_Writer():
	def __init__(self, config):
		self.config = config
		


	def add_row(self, tablename, rowdict):
		# This function adds a dictionary row to the specified table 
		# in the CRES database
		print 'add_row( tablename, rowdict )'
		print 'tablename: ', tablename
		print 'rowdict: ', rowdict

		# filter out keys that are not column names
		# you have to add new columns in the sqladmin page
		cursor.execute("describe %s" % tablename)
		allowed_keys = set(row[0] for row in cursor.fetchall())
		keys = allowed_keys.intersection(rowdict)

		if len(rowdict) > len(keys):
			unknown_keys = set(rowdict) - allowed_keys
			print "\n\nskipping keys:", ", ".join(unknown_keys)

		columns = "`" + "`,`".join(keys) + "`"

		values_template = ", ".join(["%s"] * len(keys))
		values = tuple(rowdict[key] for key in keys)

		sql = "insert into %s (%s) values %s" % (
			tablename, columns, values)

		print "\n This is the SQL line: ", sql
		cursor.execute(sql)
		db.commit()
		

	def delete_row(self, tablename, column_to_del, value):
		print "delete_row(self, tablename, column_to_del, value)"
		print '\ntablename: ', tablename
		print 'column_to_del: ', column_to_del
		print "value: ", value

		deleter = 'DELETE FROM %s WHERE `%s` = "%s"' % (tablename, column_to_del, value) 
		
		print '\n  ------************------'
		print "\nDeleter: ", deleter
		print "\n 	Are you sure?"
		ask = raw_input("	YES OR NO\n\n  ------************------\n\n")

		if ask == "" or ask == "y":
			cursor.execute(deleter)
			db.commit()

		else:
			"You did not confirm the deletion, try again bro!"
		

	def fields(self, tablename):
		# db = mysql.connector.connect(**self.config)
		# cursor = db.cursor()
		print "\nThis is Sql_Writer.fields()"
		cursor.execute("describe %s" % tablename)
		allowed_keys = set(row[0] for row in cursor.fetchall())
		return allowed_keys

	def names(self):
		# This little bugger makes the master names lists for other scripts
		cursor.execute("SELECT `Name` FROM `Locations`")
		namer = [n[0] for n in cursor.fetchall()]
		print "\nNames: ", namer, "\n"
		self.names_list = namer
		self.master_names = namer
		return namer

	def route_informer(self, place_to_lookup):
		# Grab the Address, city zip and email... for the route maker
		squeeky = 'SELECT `Address`, `City`, `Zip`, `Email`, `Phone Number`, `Contact`, `Last Pickup`, `Charity`, `Total Donation`, `Notes` FROM `Locations` WHERE `Name` = "%s"' % (place_to_lookup)
		cursor.execute(squeeky)
		route_info = cursor.fetchall()
		print "route info: ", route_info[0]
		return route_info[0]


	def sum_donations_by_restaurant(self):
		# dondb = mysql.connector.connect(**self.config)
		self.names()
		doncursor = db.cursor()
		print "\n\nThis is sum_donations()"
		total_donations = []
		c = 0
		# print "\n\n", self.master_names, "\n\n"
		for n in self.master_names:
			sqller = 'SELECT `Location`, SUM(`Expected Donation`), `Charity` FROM Pickups WHERE `Location` = "%s" ' % (n)
			doncursor.execute(sqller)
			fetcher = doncursor.fetchall()
			if fetcher[0][0] != None:
				print fetcher[0][0], "Got added" ,
				total_donations.append( (fetcher[0][0], fetcher[0][1], fetcher[0][2])  )
				print "Fetcher: ", fetcher		
		# print '\n\n', total_donations , '\n\n'
		# Reformat total_donations into a dictionary
		total_donations = { key:(round(float(value),2) , x) for key, value, x in  total_donations }	
		
		# # total_donations is a dictionary of donation totals using restaurant names as the keys
		# #	and the values are tuples in the for of (total, carity)
		for key in total_donations:
			doer = 'UPDATE `Locations` SET `Total Donation`= %s WHERE `Name` = "%s"' % (  total_donations[key][0], key )
			cursor.execute(doer)
			db.commit()
			# print key, total_donations[key]
		# Now that we've got the donations totaled and updated we should make the average column...
		
	def average_donations(self):
		print "\n\nThis is average_donations()\n"
		self.names()
		cursor = db.cursor()
		ssql = "SELECT `Location`, AVG(`Expected Donation`) FROM Pickups GROUP BY `Location`"
		cursor.execute(ssql)
		result = cursor.fetchall()
		result_dict = {str(key):round(val, 2) for key, val in result}

		print result_dict

		# Got the averages for each locations donations,
		# now to UPDATE the column

		for item in result_dict:
			cmd = 'UPDATE `Locations` SET `Average Donation`= %6.2f WHERE `Name` = "%s" ' %( result_dict[item] , item)
			print cmd
			cursor.execute(cmd)
			db.commit()

def last_pickup():
	pass
	







if __name__ == '__main__':
	print "You're running the py itself."
	writer = Sql_Writer(config)
# 	writer.add_row("Locations", loc)
#	writer.delete_row("Pickups", "Location", "Robby's Place")
	# writer.names()
	# writer.sum_donations_by_restaurant()
	writer.average_donations()

