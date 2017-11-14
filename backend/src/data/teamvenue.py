from .powerdict import PowerDict


def create_team_venue(city='', name='', timezone='', address=''):
    return TeamVenue(city, name, timezone, address)


class TeamVenue(PowerDict):

    def __init__(self, city='', name='', timezone='', address=''):
        venue = {}
        venue['city'] = city
        venue['name'] = name
        venue['timezone'] = timezone
        venue['address'] = address
        self._data = venue
