from .powerdict import PowerDict
from .teamvenue import create_team_venue


def create_team(id=0, abbreviation='', name='', fullname='', city='',
                active=False, creation_year=0, website='',
                venue=None, league_info=None):
    return Team(id, abbreviation, name, fullname, city, active, creation_year,
                website, venue, league_info)


class Team(PowerDict):

    def __init__(self, id=0, abbreviation='', name='', fullname='', city='',
                 active=False, creation_year=0, website='', venue=None,
                 league_info=None):
        team = {}
        team['id'] = id
        team['abbreviation'] = abbreviation
        team['name'] = name
        team['fullname'] = fullname
        team['city'] = city
        team['active'] = active
        team['creation_year'] = creation_year
        team['website'] = website
        team['venue'] = venue
        team['league_info'] = league_info
        self._data = team

    def set_venue(self, city, name='', timezone='', address=''):
        self.venue = create_team_venue(city, name, timezone, address)
