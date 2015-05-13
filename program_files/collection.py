# Just take the inputs and do conversions

from tabulate import tabulate
from datetime import *

# Variables we need:
# 	location
# 	height on arrivial
# 	height on departure
# 	price of oil
# 	route
# 	pickup 
# 		duration
# 		date 
# 		quality
# 		score
# 		fuel surcharge
# 			route / stops


# input should look like: 
	
# 		[ location ]

class Collection():
	"""docstring for Collection"""
	
	def __init__(self, inputs):
		# Bring in the input dictionary and store it to self for later reference
		
		self.route = {
						"Total Distance" : inputs["Total Distance"],
						"Number of Stops" : inputs["Number of Stops"]
						}

		# Given: 
		h = 36
		w = 28
		l = 48

		t_vol = 0.0043290 * l * w * h

		inputs['Gallons Arrival'] = round(0.0043290 * l * w * inputs['Arrival'] , 2)
		inputs['Gallons Departure'] = round(0.0043290 * l * w * inputs['Departure'] , 2)
		inputs['Gallons Collected'] = round(inputs['Gallons Arrival'] - inputs['Gallons Departure'] , 2)
		score = inputs['Gallons Collected'] / inputs['Gallons Arrival'] 
		inputs['Score'] = round(score * 100 , 2)

		# 7.75 lbs per gallon is set here
		lbs_collected = inputs['Gallons Collected'] * 7.75 * inputs['Quality'] / 100

		inputs['Expected Revenue'] = round(inputs['Oil Price'] * lbs_collected , 2)

		donation = inputs['Oil Price'] - inputs['Service Fee'] 

		inputs['Donation Rate'] = round(donation , 2) 
		inputs['Expected Income'] = inputs['Service Fee'] * lbs_collected
		inputs['Expected Donation'] = donation * lbs_collected
		inputs['Collectable Material'] = lbs_collected
		# for i in inputs:
		# 	print ""
		# 	print i, inputs[i]
		# inputs['Diesel Price'] = 

		# income * weight

		# inputs['Expected Donation'] = 
		

		self.indict = inputs



		def route_analizer():

			# Takes the self.route which should be in the form:
			# 	{ 
			# 		"Total Distance" : 3,
			# 		"Number of Stops" : 3,
			# 	}
			# And returns the fuel charge for the collection being initiated.

			tdist = self.route['Total Distance']
			num_stops = self.route['Number of Stops']
			diesel_price = self.indict['Diesel Price']
			mpg_truck = 8


			fuel_surcharge = float(tdist)/ mpg_truck * float(diesel_price) / int(num_stops)
			print "\nFuel Surcharge(): ", fuel_surcharge
			return fuel_surcharge


		f_surcharge = route_analizer()


		self.indict['Fuel Surcharge'] = f_surcharge

		self.indict['Miles in Route'] = self.route['Total Distance']
		self.indict['Stops in Route'] = self.route['Number of Stops']

		
		# print tabulate(  [ ( key , self.indict[key] ) for key in self.indict  ]  )


	# Make anobject that outside programs can return and use
	def run(self):
		da = datetime.now() 
		self.indict['Date'] = da.date()
		return self.indict

		






print "This is on the outside"


		





# Output:
print "End of collection\n"