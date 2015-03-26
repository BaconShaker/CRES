#! /usr/bin/python

import smtplib
import os
from os import listdir
import sys

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

# me == my email address
# you == recipient's email address
cres_email = "renewablechicago@gmail.com"
restaurant_email = "rshintani@gmail.com"

# Create message container - the correct MIME type is multipart/alternative.
msg = MIMEMultipart('alternative')
msg['Subject'] = "SImported the html this time!"
msg['From'] = cres_email
msg['To'] = restaurant_email

logo_file = "CRES_LOGO copy.jpg"
fp = open(logo_file, 'rb')
img = MIMEImage(fp.read())
fp.close()
img.add_header('Content-ID', logo_file)


# Create the body of the message (a plain-text and an HTML version).
text = "Hi!\nSpanky!\nHere is the link you wanted:\nhttp://www.python.org"
html = open("CRES_letter/to_restaurants.html")
html = html.read()




# Record the MIME types of both parts - text/plain and text/html.
part1 = MIMEText(text, 'plain')
part2 = MIMEText(html, 'html')
print "1"
# Attach parts into message container.
# According to RFC 2046, the last part of a multipart message, in this case
# the HTML message, is best and preferred.
msg.attach(part1)
msg.attach(part2)
msg.attach(img)
print "2"
# Send the message via local SMTP server.
s = smtplib.SMTP('smtp.gmail.com:587')
print "3"
s.starttls()
s.login('renewablechicago@gmail.com','WhitneyYoung')
print "4"
# sendmail function takes 3 arguments: sender's address, recipient's address
# and message to send - here it is sent as one string.
print msg.as_string()
s.sendmail(cres_email, restaurant_email, msg.as_string())

s.quit()