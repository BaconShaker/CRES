# Just take the inputs and do conversions

from tabulate import tabulate

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

		inputs['Gallons on Arrival'] = round(0.0043290 * l * w * inputs['Height (ARRIVAL): '] , 2)
		inputs['Gallons on Departure'] = round(0.0043290 * l * w * inputs['Height (DEPARTURE): '] , 2)
		inputs['Gallons Collected'] = round(inputs['Gallons on Arrival'] - inputs['Gallons on Departure'] , 2)
		score = inputs['Gallons Collected'] / inputs['Gallons on Arrival'] 
		inputs['Pickup Score'] = round(score * 100 , 2)

		# 7.75 lbs per gallon is set here
		lbs_collected = inputs['Gallons Collected'] * 7.75 * inputs['Quality (0 - 100): '] / 100

		inputs['Expected Revenue'] = round(inputs['Oil Price'] * lbs_collected , 2)

		donation = inputs['Oil Price'] - inputs['Service Fee'] 

		inputs['Donation Rate'] = round(donation , 2) 
		inputs['Expected Income'] = inputs['Service Fee'] * lbs_collected
		inputs['Expected Donation'] = donation * lbs_collected
		inputs['Collectable Material'] = lbs_collected

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

			print tdist
			print num_stops
			print diesel_price


			fuel_surcharge = float(tdist)/ mpg_truck * float(diesel_price) / int(num_stops)

			return fuel_surcharge


		f_surcharge = route_analizer()


		self.indict['Fuel Surcharge'] = f_surcharge

		self.indict['Miles in Route'] = self.route['Total Distance']
		self.indict['Stops on Route'] = self.route['Number of Stops']

		print "\n\n\n"
		print tabulate(  [ ( key , self.indict[key] ) for key in self.indict  ]  )


	# Make anobject that outside programs can return and use
	def run(self):
		return self.indict

		






print "This is on the outside"


		





# Output:
print "End of collection\n"