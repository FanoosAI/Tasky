from opsdroid.cli.start import start
import googleAPI
from googleAPI import get_events
import datetime


def setup():
    googleAPI.init()
    #  an RFC3339 timestamp with mandatory time zone offset, e.g., 2011-06-03T10:00:00-07:00
    t = datetime.datetime(year=2022, month=1, day=1)
    events = get_events.list_events(t, t + datetime.timedelta(days=365))
    print(len(events))


if __name__ == '__main__':
    setup()
    # start()
