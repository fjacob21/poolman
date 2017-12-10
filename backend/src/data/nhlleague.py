from .powerdict import PowerDict
from .nhlleague_year import NHLLeagueYear


def create_league(name, desc='', website=''):
    return NHLLeague(name, desc, website)


class NHLLeague(PowerDict):

    def __init__(self, name='', desc='', website=''):
        league = {}
        league['name'] = name
        league['desc'] = desc
        league['website'] = website
        league['teams'] = None
        league['years'] = {}
        self._data = league

    def add_year(self, year):
        self.years[year] = NHLLeagueYear(year)
        return self.years[year]
