from datetime import datetime

from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import googleAPI
import logging


def add_event(start_time: datetime, end_time: datetime, title: str, description: str):
    service = build("calendar", "v3", credentials=googleAPI.CREDENTIALS)
    try:
        events_result = (
            service.events()
            .insert(
                calendarId='primary',
                start=start_time.astimezone().isoformat(),
                end=end_time.astimezone().isoformat(),
                summary=title,
                description=description
            )
        ).execute()

    except HttpError as err:
        logging.error(f"ERROR: {err}")
    finally:
        service.close()
