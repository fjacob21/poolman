from datetime import datetime
from dateutil import tz


def string_to_date(date):
    from_zone = tz.gettz('UTC')
    to_zone = tz.gettz('America/New_York')
    utc = datetime.strptime(date, '%Y-%m-%dT%H:%M:%SZ')
    utc = utc.replace(tzinfo=from_zone)
    return utc.astimezone(to_zone)


def date_to_string(date):
    to_zone = tz.gettz('UTC')
    return date.astimezone(to_zone).strftime('%Y-%m-%dT%H:%M:%SZ')


def now():
    to_zone = tz.gettz('America/New_York')
    return datetime.now(tz.tzlocal()).astimezone(to_zone)


def date(year, month, day, hour=0, minute=0, second=0,
         tzinfo=tz.gettz('America/New_York')):
    return datetime(year, month, day, hour, minute, second, tzinfo=tzinfo)
