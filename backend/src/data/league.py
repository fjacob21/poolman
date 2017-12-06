from .powerdict import PowerDict
from .league_year import LeagueYear


def create_league(name, desc='', website=''):
    return League(name, desc, website)


class League(PowerDict):

    def __init__(self, name, desc='', website=''):
        league = {}
        league['name'] = name
        league['desc'] = desc
        league['website'] = website
        league['teams'] = None
        league['years'] = {}
        self._data = league

    def add_year(self, year):
        self.years[year] = LeagueYear(year)
        return self.years[year]
