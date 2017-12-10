from .powerdict import PowerDict
from .matchuptree import create_matchup_tree


class LeagueYear(PowerDict):

    def __init__(self, year=0):
        league_year = {}
        league_year['year'] = year
        league_year['standings'] = {}
        league_year['matchups'] = create_matchup_tree()
        league_year['teams_games'] = {}
        self._data = league_year

    @property
    def is_year_finished(self):
        return False
