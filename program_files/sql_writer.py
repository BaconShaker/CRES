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
	def __init__(self):
		self.config = {
		  'user': 'root',
		  'password': 'Illini032',
		  'host': 'localhost',
		  'database': 'CRES',
		  'raise_on_warnings': True,
		  'port': 8888
		}


	def add_row(self, tablename, rowdict):
		# This function adds a dictionary row to the specified table 
		# in the CRES database

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

		# print "\n This is the SQL line: ", sql
		cursor.execute(sql)
		db.commit()

	def delete_row(self, tablename, column_to_del, chooser):
		db = mysql.connector.connect(**self.config)
		cursor = db.cursor()
		deleter = "DELETE FROM %s WHERE %s = `%s`" % (tablename, column_to_del, chooser) 
		cursor.execute(deleter)
		db.commit()



if "__main__" == '__main__':
	print "hello"
	writer = Sql_Writer()
	# writer.add_row("Locations", loc)
	writer.delete_row("Locations", "Name", loc['Name'])

