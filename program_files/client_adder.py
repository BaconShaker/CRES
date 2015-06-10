#!/Users/AsianCheddar/sql_try/bin/python

# This is a script that keeps track of client leads, contact info and such.
# It should also send emails and schedule follow ups (Google Cal?). 


from datetime import datetime
import os

from apiclient.discovery import build
from httplib2 import Http
import oauth2client
from oauth2client import client
from oauth2client import tools

try:
    import argparse
    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
    flags = None

SCOPES = 'https://www.googleapis.com/auth/calendar'
CLIENT_SECRET_FILE = os.path.expanduser('~/client_secret.json')
APPLICATION_NAME = 'Google Calendar API Quickstart'


def get_credentials():
    """Gets valid user credentials from storage.

    If nothing has been stored, or if the stored credentials are invalid,
    the OAuth2 flow is completed to obtain the new credentials.

    Returns:
        Credentials, the obtained credential.
    """
    home_dir = os.path.expanduser('~')
    credential_dir = os.path.join(home_dir, '.credentials')
    if not os.path.exists(credential_dir):
        os.makedirs(credential_dir)
    credential_path = os.path.join(credential_dir,
                                   'calendar-quickstart.json')

    store = oauth2client.file.Storage(credential_path)
    credentials = store.get()
    if not credentials or credentials.invalid:
        flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
        flow.user_agent = APPLICATION_NAME
        if flags:
            credentials = tools.run_flow(flow, store, flags)
        else: # Needed only for compatability with Python 2.6
            credentials = tools.run(flow, store)
        print 'Storing credentials to ' + credential_path

    return credentials

def main():
    """Shows basic usage of the Google Calendar API.

    Creates a Google Calendar API service object and outputs a list of the next
    10 events on the user's calendar.
    """
    credentials = get_credentials()

    service = build('calendar', 'v3', http=credentials.authorize(Http()))

    now = datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time
    print 'Getting the upcoming 10 events'
    eventsResult = service.events().list(
        calendarId='primary', timeMin=now, maxResults=10, singleEvents=True,
        orderBy='startTime').execute()
    events = eventsResult.get('items', [])

    if not events:
        print 'No upcoming events found.'
    for event in events:
        start = event['start'].get('dateTime', event['start'].get('date'))
        print '\n\n', start, event['summary']
        # print "***", event["attendees"].get('displayName') ,"***"

        # attendees = event.get('attendees')
        # print attendees

        for thing in event:
        	if thing == "attendees":
        		print thing
        		for p in event[thing]:
        			# print p
        			print "		", p["displayName"], p['responseStatus']


def make_event():
    credentials = get_credentials()

    service = build('calendar', 'v3', http=credentials.authorize(Http()))

    event = {
        'summary': '(TEST)Gotta do a pickup!',
        'location': '800 Howard St., San Francisco, CA 94103',
        'description': "(THIS IS A TEST)Don't forget the paper towels",
        'start': {
            'dateTime': '2015-06-28T09:00:00-07:00',
            'timeZone': 'America/Los_Angeles',
        },
        'end': {
            'dateTime': '2015-06-28T17:00:00-07:00',
            'timeZone': 'America/Los_Angeles',
        },
        # 'recurrence': ['RRULE:FREQ=DAILY;COUNT=2'],
        'attendees': [
            {
            'email': 'rshintani@gmail.com',
            "displayName": "The Robster"
            },
            {
            'email': 'mmirabelli88@gmail.com',
            "displayName": "Mikey"
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

    event = service.events().insert(calendarId='primary', body=event).execute()
    print 'Event created: %s' % (event.get('htmlLink'))

def connect():
	# Authorize server-to-server interactions from Google Compute Engine.
	from oauth2client import gce

	credentials = gce.AppAssertionCredentials(
	scope='https://www.google.com/m8/feeds')
	http = credentials.authorize(Http())
	print http

	import atom.data
	import gdata.data
	import gdata.contacts.client
	import gdata.contacts.data

def PrintAllContacts(gd_client):
  feed = gd_client.GetContacts()
  for i, entry in enumerate(feed.entry):
    print '\n%s %s' % (i+1, entry.name.full_name.text)
    if entry.content:
      print '    %s' % (entry.content.text)
    # Display the primary email address for the contact.
    for email in entry.email:
      if email.primary and email.primary == 'true':
        print '    %s' % (email.address)
    # Show the contact groups that this contact is a member of.
    for group in entry.group_membership_info:
      print '    Member of group: %s' % (group.href)
    # Display extended properties.
    for extended_property in entry.extended_property:
      if extended_property.value:
        value = extended_property.value
      else:
        value = extended_property.GetXmlBlob()
      print '    Extended Property - %s: %s' % (extended_property.name, value)

if __name__ == '__main__':
    main()
    # make_event()
    # PrintAllContacts(connect())
    # PrintAllContacts(get_credentials())