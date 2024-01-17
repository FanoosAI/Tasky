import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow

import yaml

CREDENTIALS = None


def init():
    global CREDENTIALS
    google_config = yaml.safe_load(open('google_config.yaml'))
    scopes = google_config['SCOPES']
    credentials_file = google_config['CREDENTIALS_FILE']

    if os.path.exists('token.json'):
        CREDENTIALS = Credentials.from_authorized_user_file("token.json", scopes)

    if not CREDENTIALS or not CREDENTIALS.valid:
        if CREDENTIALS and CREDENTIALS.expired and CREDENTIALS.refresh_token:
            CREDENTIALS.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(credentials_file, scopes)
            CREDENTIALS = flow.run_local_server(port=8080)
        with open('token.json', 'w') as token:
            token.write(CREDENTIALS.to_json())
