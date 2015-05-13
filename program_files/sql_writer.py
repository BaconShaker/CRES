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





class Sql_Writer():
	def __init__(self, config):
		self.config = config
		


	def add_row(self, tablename, rowdict):
		# This function adds a dictionary row to the specified table 
		# in the CRES database

		print 'add_row( tablename, rowdict )'
		print 'tablename: ', tablename
		print 'rowdict: ', rowdict

		db = mysql.connector.connect(**self.config)
		cursor = db.cursor()

		# filter out keys that are not column names
		cursor.execute("describe %s" % tablename)
		allowed_keys = set(row[0] for row in cursor.fetchall())
		keys = allowed_keys.intersection(rowdict)


		if len(rowdict) > len(keys):
			unknown_keys = set(rowdict) - allowed_keys
			print "skipping keys:", ", ".join(unknown_keys)

		columns = "`" + "`,`".join(keys) + "`"

		values_template = ", ".join(["%s"] * len(keys))
		values = tuple(rowdict[key] for key in keys)

		sql = "insert into %s (%s) values %s" % (
			tablename, columns, values)

		print "\n This is the SQL line: ", sql
		cursor.execute(sql)
		db.commit()
		db.close()

	def delete_row(self, tablename, column_to_del, value):
		print "delete_row(self, tablename, column_to_del, value)"
		print '\n tablename: ', tablename
		print 'column_to_del: ', column_to_del
		print "value: ", value

		db = mysql.connector.connect(**self.config)
		cursor = db.cursor()
		deleter = "DELETE FROM %s WHERE `%s` = '%s'" % (tablename, column_to_del, value) 
		print "\nDeleter: ", deleter
		cursor.execute(deleter)
		db.commit()
		db.close()

	def fields(self, tablename):
		db = mysql.connector.connect(**self.config)
		cursor = db.cursor()
		cursor.execute("describe %s" % tablename)
		allowed_keys = set(row[0] for row in cursor.fetchall())

		print allowed_keys

		db.close()
		return allowed_keys

	def names(self):
		db = mysql.connector.connect(**self.config)
		cursor = db.cursor()
		cursor.execute("SELECT `Name` FROM `Locations`")
		names = [n[0] for n in cursor.fetchall()]
		print "\nNames: ", names
		return names

	def route_informer(self, place_to_lookup):
		db = mysql.connector.connect(**self.config)
		cursor = db.cursor()
		squeeky = 'SELECT `Address`, `City`, `Zip`, `Email`, `Phone Number`, `Contact`, `Last Pickup`, `Charity`, `Total Donation`, `Notes` FROM `Locations` WHERE `Name` = "%s"' % (place_to_lookup)
		cursor.execute(squeeky)
		route_info = cursor.fetchall()
		print "route info: ", route_info[0]
		db.close()
		return route_info[0]





if "__main__" == '__main__':
	print "hello"
	config = {
		  'user': 'root',
		  'password': 'Illini032',
		  'host': 'localhost',
		  'database': 'CRES',
		  'raise_on_warnings': True,
		  'port': 8888
		}
	writer = Sql_Writer(config)
	# writer.add_row("Locations", loc)
	# writer.delete_row("Locations", "Name", loc['Name'])
	writer.names()

