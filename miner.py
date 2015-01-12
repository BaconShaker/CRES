
import csv 
from tabulate import tabulate
import os.path
from datetime import datetime
import urllib2
from bs4 import BeautifulSoup
import csv
	

print ""
print "price_lookup:"
response = urllib2.urlopen('http://www.ams.usda.gov/mnreports/nw_ls442.txt')

data = response.read()

info = response.info()

# response = urllib2.urlopen('http://www.ams.usda.gov/mnreports/nw_ls442.txt')
soup = BeautifulSoup(data)

# text = soup.get_text()
# print soup.prettify(formatter= 'html')
content =  soup.contents
reader = csv.reader(content)
for line in reader:
	print line

# print content



response.close()