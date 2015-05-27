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
		lbs_collected = inputs['Gallons Collected'] * 7.75 

		inputs['Expected Revenue'] = round(inputs['Oil Price'] * lbs_collected , 2)

		donation = inputs['Oil Price'] - inputs['Service Fee'] 

		inputs['Donation Rate'] = round(donation , 2) 
		inputs['Expected Income'] = inputs['Service Fee'] * lbs_collected
		inputs['Expected Donation'] = round( donation * lbs_collected * inputs['Quality'] / 100 , 2) 
		inputs['Collectable Material'] = lbs_collected
		inputs["Penalty"] = round(inputs['Expected Revenue'] - (inputs['Expected Income'] + inputs['Expected Donation']) ,2)

		# Need to account for the penalty associated with poor quality in the income that CRES will get
		inputs['Expected Income'] = round(inputs['Expected Income'] + inputs['Penalty'] , 2)
		
		

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
			fuel_surcharge = round(fuel_surcharge , 2)
			print "\nFuel Surcharge(): ", fuel_surcharge
			return fuel_surcharge


		f_surcharge = route_analizer()

		print "\n\n THTHTHTHTHT\n\n"
		self.indict['Fuel Surcharge'] = f_surcharge

		self.indict['Miles in Route'] = self.route['Total Distance']
		self.indict['Stops in Route'] = self.route['Number of Stops']

		# Need to adjust expected income and donation amounts

		self.indict['Expected Income'] = self.indict['Expected Income'] + f_surcharge
		self.indict['Expected Donation'] = self.indict['Expected Donation'] - f_surcharge

		
		# print tabulate(  [ ( key , self.indict[key] ) for key in self.indict  ]  )

		#This is a debugging checker.
		# Make sure the total revenue = cres + donation + f_surcharge

		# print "This 0 =", self.indict['Expected Revenue'] - self.indict['Expected Income'] - self.indict['Expected Donation'] - self.indict['Fuel Surcharge']

	# Make anobject that outside programs can return and use
	def run(self):
		if len(self.indict["Pickup Date"]) == 0:
			da = datetime.now().date()
			self.indict['Pickup Date'] = str(da)
			
		print '\n\n'  , self.indict ,  "\n\n"


		return self.indict

		






print "This is on the outside"


		





# Output:
print "End of collection\n"