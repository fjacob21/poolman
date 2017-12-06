from .powerdict import PowerDict
from .matchuptree import create_matchup_tree


class LeagueYear(PowerDict):

    def __init__(self, year):
        league_year = {}
        league_year['year'] = year
        league_year['standings'] = {}
        league_year['matchups'] = create_matchup_tree()
        league_year['teams_games'] = {}
        self._data = league_year
