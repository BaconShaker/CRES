#!/usr/bin/python

from googlemaps import Client
import json


origins = '2256 N Kedzie BLVD 60647'
destinations = '2021 W Fulton 60612'

this = Client(key = 'AIzaSyCDhR6raMscym9p0VG55-ka_p1IP9Dq9q0')

dirs =  this.directions(origins, destinations)

for line in dirs:
	print json.dumps(line, sort_keys = True)
		