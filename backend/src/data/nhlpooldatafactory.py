from .pooldatafactory import PoolDataFactory
from .nhlmatchup import NHLMatchup
from .nhlleague import NHLLeague


class NHLPoolDataFactory(PoolDataFactory):

    def __init__(self):
        PoolDataFactory.__init__(self)

    def create_matchup(self, id=0, round=0, home=0, away=0,
                       playoff=None, season=None):
        return NHLMatchup(id, round, home, away, playoff, season)

    def create_league(self, name, desc='', website=''):
        return NHLLeague(name, desc, website)
