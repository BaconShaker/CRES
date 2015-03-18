#!/usr/bin/python


# This is the googlemaps api version of jedi.py

from googlemaps import Client
import json
from tabulate import tabulate


# start = '2256 n kedzie blvd 60647'
# stop = '2804 w logan blvd 60647'

class GoogleMap():
	"""docstring for Leg"""
	def __init__(self, trip, *args):
		# Trip must be a list of addresses, the class will take care of the waypointing. 

		tripper = [  field[0] +" "+ field[1]  +" "+ field[2]  for field in trip  ]
		self.start = tripper[0]
		self.stop = tripper[len(tripper) - 1 ]
		# self.start = trip[0][0] , trip[0][1], float(trip[0][2])
		# self.stop = trip[len(trip) - 1][0] , trip[len(trip) - 1][1] , trip[len(trip) - 1][2]  

		# self.start = 
		# self.stop = 
		print trip
		self.waypoints = [ wp[0] +" "+ wp[1]  +" "+ wp[2]  for wp in trip[1:len(trip) - 1] ]

		print "\n\n"
		print "Start: ", self.start
		print "Waypoints: " , self.waypoints
		print "Stop: " , self.stop
		
		print "________-----------_______"
		
		
	def google_directions( self ):

		# initalize a googlemaps object
		gmap = Client('AIzaSyCDhR6raMscym9p0VG55-ka_p1IP9Dq9q0')

		print '\n\n'
		print "This is waypoints::::: " , self.waypoints

		# call the .directions() funciton on Client, save in a list
		# See if we should use waypoint optimixzing?

		directions = gmap.directions(self.start, self.stop, waypoints = self.waypoints)

		print "\n\n\n******************************\n\n\n"


		# print directions['Directions']['Distance']["meters"]


		print "\n\n\n******************************\n\n\n"

		for item in directions: 
			# Iterate through the list
			
			steps =  item['legs'][0]['steps'] 
			display = []
			turn = 0
			leg = 0
			for step in steps:
				to_go = step['distance']['text']
				turn = turn + 1
				words = step['html_instructions']
				words = words.replace( '<b>' , ' ')
				words = words.replace( '</b>' , ' ')
				words = words.replace( '<div style="font-size:0.9em">' , '')
				words = words.replace( '</div>' , ' ' )
				display.append([turn,  to_go, words])
			# print display
			

			tabs = ["Turn", "Distance", "Instruction"]

			tab = tabulate(display, headers = tabs, tablefmt = "simple")

			# print tab
		# return directions
		return tab
