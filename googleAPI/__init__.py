import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import yaml


def init():
    google_config = yaml.safe_load(open('google_config.yaml'))
    scopes = google_config['SCOPES']
    credentials_file = google_config['CREDENTIALS_FILE']
    creds = None

    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file("token.json", scopes)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(credentials_file, scopes)
            creds = flow.run_local_server(port=8080)
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    try:
        service = build("calendar", "v3", credentials=creds)
        print("Upcoming 10 services")
        events_result = (
            service.events()
            .list(
                calendarId='primary',
                timeMin='2021-10-01T00:00:00+01:00',
                maxResults=10,
                singleEvents=True,
                orderBy='startTime'
            ).execute()
        )
        events = events_result.get('items', [])
        if not events:
            print("No upcoming events found.")
            return
        for event in events:
            start = event['start'].get('dateTime', event['start'].get('date'))
            print(start, event['summary'])

    except HttpError as err:
        print("ERROR: ", err)


