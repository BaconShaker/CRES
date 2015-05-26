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

		# db = mysql.connector.connect(**self.config)
		# cursor = db.cursor()

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
		# db.close()

	def delete_row(self, tablename, column_to_del, value):
		print "delete_row(self, tablename, column_to_del, value)"
		print '\ntablename: ', tablename
		print 'column_to_del: ', column_to_del
		print "value: ", value

		# db = mysql.connector.connect(**self.config)
		# cursor = db.cursor()
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
		# db.close()

	def fields(self, tablename):
		# db = mysql.connector.connect(**self.config)
		# cursor = db.cursor()
		cursor.execute("describe %s" % tablename)
		allowed_keys = set(row[0] for row in cursor.fetchall())

		print allowed_keys

		# db.close()
		return allowed_keys

	def names(self):
		# db = mysql.connector.connect(**self.config)
		# cursor = db.cursor()
		cursor.execute("SELECT `Name` FROM `Locations`")
		names = [n[0] for n in cursor.fetchall()]
		print "\nNames: ", names
		self.names = names
		# db.close()
		return names

	def route_informer(self, place_to_lookup):
		# db = mysql.connector.connect(**self.config)
		# cursor = db.cursor()
		squeeky = 'SELECT `Address`, `City`, `Zip`, `Email`, `Phone Number`, `Contact`, `Last Pickup`, `Charity`, `Total Donation`, `Notes` FROM `Locations` WHERE `Name` = "%s"' % (place_to_lookup)
		cursor.execute(squeeky)
		route_info = cursor.fetchall()
		print "route info: ", route_info[0]
		# db.close()
		return route_info[0]

	def update_supporters():
		# This attribute goes through all the locations and allocates the locations
		# to their respective Charity
		pass

	def sum_donations_by_restaurant(self):
		print "This is sum_donations()"
		total_donations = []
		c = 0
		print self.names
		for n in self.names:
			print "n: ", n
			sqller = 'SELECT `Location`, SUM(`Expected Donation`), `Charity` FROM Pickups WHERE `Location` = "%s" ' % (n) 
			cursor.execute(sqller)
			fetcher = cursor.fetchall()
			print fetcher
			if fetcher[0][0] != None:
				print fetcher[0][0], "Got added"
				total_donations.append( (fetcher[0][0], fetcher[0][1], fetcher[0][2])  )
		print '\n\n', total_donations , '\n\n'

		total_donations = { key:(round(float(value),2) , x) for key, value, x in  total_donations }	
		
		# total_donations is a dictionary of donation totals using restaurant names as the keys
		#	and the values are tuples in the for of (total, carity)

		for key in total_donations:
			doer = 'UPDATE `Locations` SET `Total Donation`= %s WHERE `Name` = "%s"' % (  total_donations[key][0], key )
			cursor.execute(doer)
			db.commit()

			print key, total_donations[key]
		

if __name__ == '__main__':
	print "You're running the py itself."
	writer = Sql_Writer(config)
# 	writer.add_row("Locations", loc)
#	writer.delete_row("Pickups", "Location", "Robby's Place")
	writer.names()
	writer.sum_donations_by_restaurant()

