import datetime

from opsdroid.cli import start

import googleAPI
from googleAPI import get_events


def setup():
    googleAPI.init()
    t = datetime.datetime(year=2022, month=1, day=1)
    events = get_events.list_events(t, t + datetime.timedelta(days=365))
    print(len(events))


if __name__ == '__main__':
    # setup()
    start()
