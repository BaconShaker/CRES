#!/Users/AsianCheddar/sql_try/bin/python

# This file should write the user inputs from routebuilder in a MySQL database
# instead of in a csv file

import mysql.connector
from datetime import *
import numpy
import math
from client_adder import *
from all_restaurants import place_lookup



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

print "\nSuccessfully loaded sql_writer.py.\n"
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

def days_between(d1, d2):
    d1 = datetime.strptime(d1, "%Y-%m-%d")
    d2 = datetime.strptime(d2, "%Y-%m-%d")
    return abs((d2 - d1).days)


# def average_collections():
# 	print "\nThis is averageing the collections..."
# 	average_sql = """SELECT `Location`, round(AVG(`Gallons Collected`) , 2) as "Average Collection" from Pickups group by `Location`"""
# 	cursor.execute(average_sql)
# 	collection_averages = cursor.fetchall()
# 	for thing in collection_averages:
# 		mean_sql = """UPDATE Locations SET `Average Collection`= %s WHERE `Name` = "%s" """ % (thing[1], thing[0])
# 		cursor.execute(mean_sql)
# 		db.commit()


class Sql_Writer():
	def __init__(self, config):
		self.config = config

		# UPDATE the average collection column in Loations table
	def average_collections(self):
		print "\nThis is averageing the collections..."
		average_sql = """SELECT `Location`, round(AVG(`Gallons Collected`) , 2) as "Average Collection" from Pickups group by `Location`"""
		cursor.execute(average_sql)
		collection_averages = cursor.fetchall()
		for thing in collection_averages:
			mean_sql = """UPDATE Locations SET `Average Collection`= %s WHERE `Name` = "%s" """ % (thing[1], thing[0])
			cursor.execute(mean_sql)
			db.commit()
		
	def get_place_info(self):
		place_lookup("Hachi's Kitchen")

	def pickup_scheduler(self, pickup_to_schedule):

		print """
		pickup_to_schedule needs to be in the format of:
			0 summary string
			1 locaton (full address) string
			2 description string
			3 0 start date (2015-09-28)
			  1 start time (T09:00:00-07:00)
			4 0 end date (2015-09-28)
			  1 end time (T17:00:00-07:00)\n\n

			By default Robby and Mike are the only invitees. That can be changed later
		"""

		to_add = {
		    'summary': pickup_to_schedule[0],
		    'location': pickup_to_schedule[1],
		    'description': pickup_to_schedule[2],
		    'start': {
		        'dateTime': pickup_to_schedule[3][0] + 'T' + pickup_to_schedule[3][1],
		        'timeZone': 'America/Chicago',
		    },
		    'end': {
		        'dateTime': pickup_to_schedule[4][0] + 'T' + pickup_to_schedule[4][1],
		        'timeZone': 'America/Chicago',
		    },
		    # 'recurrence': ['RRULE:FREQ=DAILY;COUNT=2'],
		    'attendees': [
		        {
		        'email': 'rshintani@gmail.com',
		        "displayName": "Robby Shintani"
		        },
		        {
		        'email': 'mmirabelli88@gmail.com',
		        "displayName": "Michael Mirabelli"
		        },
		    ],
		    'reminders': {
		        'useDefault': False,
		        'overrides': [
		                    {'method': 'email', 'minutes': 24 * 60},
		                    {'method': 'sms', 'minutes': 10},
		                    ],
		        },
		    }

		# This is for the google Calendar API
		calendar = GCal()
		calendar.list_events()

	


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

	def which_charity(self, address):
		# Look up charity for Location using the address.
		sqlly = 'SELECT `Name`, `Charity` FROM `Locations` WHERE `Address` LIKE \"%'
		add_on =  address +'%"' 
		sqlly = sqlly + add_on
		print sqlly
		cursor.execute(sqlly)
		answer = cursor.fetchall()
		if answer: 
			print "Charity for", answer[0][0], ":", answer[0][1]
			print "answer: ", answer
			# if type(answer) is not list:
			# 	return answer[0]
			# else: 
			# 	return answer
			return answer[0][1]

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
		return total_donations

	def sum_donations_by_month(self, month):
		# Return a dictionary of location : (monthly donation, charity)

		# self.names()
		doncursor = db.cursor()
		print "\n\nThis is sum_donations_by_month()"
		
		monthsql = "select `Location`, SUM(`Collectable Material`) , SUM(`Gallons Collected`),  SUM(`Expected Donation`) , `charity` from Pickups where MONTHNAME(`Pickup Date`) = '%s' group by `Location`" % (month)

		doncursor.execute(monthsql)
		grabber = doncursor.fetchall()
		print grabber
		monthly_donations = { key:(int(lbs), int(gallons), round(float(tot_donation),2) , charity) for key, lbs, gallons, tot_donation, charity in  grabber }
		# print "\n\nMonthly donations: " , monthly_donations
		return monthly_donations
		
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


	def last_pickup(self, chk):
		print "\nlast_pickup()..."
		print "Passing lastpickup(0) will result in no UPDATE; passing (1) will UPDATE"
		self.names()
		cursor = db.cursor()
		launch = """SELECT 
						`Location`,
						MAX(`Pickup Date`) AS "Last Collection",
						`Arrival`,
						`Departure`,
						`Quality`,
						`Expected Income`,
						`Expected Donation`
					FROM Pickups 
					GROUP BY `Location`"""

		cursor.execute(launch)
		recent_pickups = cursor.fetchall()
		# for t in recent_pickups:
		# 	print t
		self.picker = recent_pickups

		if chk == 1:
			for pickup in recent_pickups:
				print pickup
				admin = """UPDATE Locations SET `Last Pickup`= '%s' WHERE `Name` = "%s" """ % ( pickup[1] , pickup[0] )
				print admin, '\n'
				cursor.execute(admin)
				db.commit()
		else:
			return recent_pickups

	def collection_analysis(self):
		# Finds the average number of days between pickups 
		print "\n\nThis is collection_analysis()"
		cursor = db.cursor()
		
		day_dict = {}
		gal_dict = {}

		for ent in self.names():

			finder = """SELECT 
							`Pickup Date`,
							`Gallons Collected`,
							`Arrival`,
							`Departure`,
							`Quality`,
							`Expected Income`,
							`Expected Donation`
						FROM Pickups 
						WHERE `Location` = "%s" """ % (ent)
			cursor.execute(finder)
			sparks = cursor.fetchall()
			print ent
			cou = 0
			day_list = []
			gal_list = []

			# Sparks is a list of pickups from each Location
			for spark in sparks:
				print cou, spark
				cou += 1
				
				if cou <= len(sparks) - 1:
					
					days_btw_pickups = days_between(str(sparks[cou][0]), str(spark[0]))
					day_list.append(days_btw_pickups)

					gal_list.append(sparks[cou][1])

				else:
					# Runs when the iterator gets to the end of the pickups/restaurant
					# 	It's because you want the days between..

					ziplist = zip(day_list, gal_list)
					print ziplist
					gal_per_day = []
					for z in ziplist:
						gal_per_day.append(z[1]/z[0])

					# Predict next pickup by actual gallons collectd.
					gal_per_day =round(numpy.mean(gal_per_day), 0)
					print "gal_per_day", gal_per_day
					fill_time_by_gallons = round(200/gal_per_day , 0)
					

					print "Fill Time by gallons collected: " , fill_time_by_gallons  , "days"
					
					# "Fill time" by actual pickups--more like actual pickup average
					average_fill_time = round(numpy.mean(day_list), 0)
					
					if not math.isnan(average_fill_time):
						fill_time_by_gallons = int(fill_time_by_gallons)
						print "Average time between pickups: ", int(average_fill_time), "days."
						print "Fill Time by gallons collected: " , fill_time_by_gallons  , "days."
						day_dict[ent] = average_fill_time
						gal_dict[ent] = fill_time_by_gallons
			print ""
		print "Day_dict: ", day_dict
		
		print "Gal_dict: ", gal_dict

		# Making sure self.picker is intact but not writing... 
		self.last_pickup(0)

		for key in day_dict:
			print key, day_dict[key], gal_dict[key]
			planner = 'UPDATE Locations SET `Fill Time` = %s, `Fill Time Gallons` = %s WHERE `Name` = "%s"' % ( day_dict[key] , gal_dict[key], key )
			cursor.execute(planner)
			db.commit()

			print planner 

			looklast = 'SELECT `Name`, `Last Pickup` from Locations where `Name` = "%s" ' % (key)
			cursor.execute(looklast)
			looklast = cursor.fetchall()
			nextpick = {key: las[1]+ timedelta(day_dict[key]) for las in looklast}
			nextpick_gal = {key: las[1]+ timedelta(gal_dict[key]) for las in looklast}
			print "nextpick: " , nextpick
			print "nextpick_gal: " , nextpick_gal


			next = """UPDATE Locations SET `Next Pickup` = "%s", `Next Pickup Gallons` = "%s" where `Name` = "%s" """ % (nextpick[key], nextpick_gal[key] ,key )
			print next
			cursor.execute(next)
			db.commit()

		print "\n"*5 
		for r in day_dict:
			print "We go to", r , "every", day_dict[r], "but it should take ~", gal_dict[r] ,"days to fill.\n"
		return day_dict


	def oil_on_hand(self):
		# This is going to return the expected volume of oil on hand
		seeql = """SELECT SUM(`Gallons Collected`) FROM Pickups """
		cursor.execute(seeql)
		volume = cursor.fetchall()
		return int(volume[0][0])


if __name__ == '__main__':
	print "You're running the py itself."
	writer = Sql_Writer(config)
# 	writer.add_row("Locations", loc)
#	writer.delete_row("Pickups", "Location", "Robby's Place")
	# writer.names()
	# writer.sum_donations_by_restaurant()
	# writer.average_donations()
	# writer.last_pickup()
	# writer.collection_analysis()
	print writer.oil_on_hand()
	# writer.get_place_info()
	writer.which_charity("2021 W. Fulton Chicago")

	
	# writer.collection_analysis()

	# Doesn't work:

	# writer.pickup_scheduler()
	

