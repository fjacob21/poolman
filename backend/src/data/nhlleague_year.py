from .powerdict import PowerDict
from .matchuptree import create_matchup_tree
from .league_year import LeagueYear


class NHLLeagueYear(LeagueYear):

    def __init__(self, year=0):
        LeagueYear.__init__(self, year)

    @property
    def is_year_finished(self):
        if len(self.standings) == 0:
            return False
        for standing in self.standings.values():
            if standing.games_played != 82:
                return False
        return True
