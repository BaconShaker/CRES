#!/envs/CRES/bin/python

# GET CREDENTIALS FOR GOOGLE API
import os, oauth2client


def get_credentials():
    print "This is inside the function"
    """Gets valid user credentials from storage.

    If nothing has been stored, or if the stored credentials are invalid,
    the OAuth2 flow is completed to obtain the new credentials.

    Returns:
        Credentials, the obtained credential.
    """
    scopes = 	['https://spreadsheets.google.com/feeds',
    			'https://www.googleapis.com/auth/calendar']

    home_dir = os.path.expanduser('~')
    credential_dir = os.path.expanduser('~/google_creds')
    if not os.path.exists(credential_dir):
        os.makedirs(credential_dir)
    credential_path = os.path.join(credential_dir,
                                   'sheets_credentials.json')

    APPLICATION_NAME = "route_handler"
    CLIENT_SECRET_FILE = os.path.expanduser('~/google_creds/client_secret.json')
    store = oauth2client.file.Storage(credential_path)
    credentials = store.get()
    if not credentials or credentials.invalid:
        flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, scopes)
        flow.user_agent = APPLICATION_NAME
        if flags:
            credentials = tools.run_flow(flow, store, flags)
        else: # Needed only for compatability with Python 2.6
            credentials = tools.run(flow, store)
        print 'Storing credentials to ' + credential_path

    return credentials