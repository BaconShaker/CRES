# CRES
CRES Python Repo
The main current .py file is called gui_class.py as of 3/9/15.

The program requires there to be a GoogleDrive folder to be in the root file of the filesystem. 
Check if the file is in the correct directory, open Terminal and type cd then 'enter'
Next type 'ls'. If you have a file called GDrive, it should pop up in the list provided. The Drive folder needs to be called 'GDrive'


I will put a list of modules that need to be downloaded here soon. Use PIP install to get all of them. 

		from tabulate import tabulate #makes the nice tables
		import os.path #pathfinder
		import time #this is for any delays I want
		import sys
		import os
		from os import listdir
		import csv
		import urllib
		import urllib2
		from bs4 import BeautifulSoup           # pip install BeautifulS
		from Tkinter import *
		import ttk
		from datetime import date

Find get-pip.py @ https://bootstrap.pypa.io/get-pip.py



The main menu is still in text form but the pickup is run in GUI format. 

I have it set up to build a list of input dictionaries and adds them to /GDrive/cres_sheets/location name