from datetime import datetime

from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import googleAPI
import logging


def list_events(start_time: datetime, end_time: datetime, max_results=10):
    service = build("calendar", "v3", credentials=googleAPI.CREDENTIALS)
    try:
        events_result = (
            service.events()
            .list(
                calendarId='primary',
                timeMin=start_time.astimezone().isoformat(),
                timeMax=end_time.astimezone().isoformat(),
                maxResults=max_results,
                singleEvents=True,
                orderBy='startTime'
            ).execute()
        )
        events = events_result.get('items', [])
        return events if events else []
    except HttpError as err:
        logging.error(f"ERROR: {err}")
    finally:
        service.close()
