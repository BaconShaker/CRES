#!/usr/bin/python


# This is the googlemaps api version of jedi.py

from googlemaps import Client
import json
from tabulate import tabulate


start = '2256 n kedzie blvd 60647'
stop = '2804 w logan blvd 60647'


def google_directions( start, stop ):

	# initalize a googlemaps object
	gmap = Client('AIzaSyCDhR6raMscym9p0VG55-ka_p1IP9Dq9q0')

	print '\n\n'

	# call the .directions() funciton on Client, save in a list

	directions = gmap.directions(start, stop)

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

		print tab
	return directions

robby = google_directions(start, stop)

print robby