from .game import GAME_STATE_SCHEDULED, GAME_STATE_FINISHED
from .matchupresult import MatchupResult
from .powerdict import PowerDict


def create_matchup(id=0, round=0, home=0, away=0, start='',
                   playoff=None, season=None):
    return Matchup(id, round, home, away, start, playoff, season)


class Matchup(PowerDict):

    def __init__(self, mid=0, round=0, home=0, away=0, start='',
                 playoff=None, season=None):
        if not playoff:
            playoff = MatchupResult()
        if not season:
            season = MatchupResult()
        matchup = {}
        matchup['id'] = mid
        matchup['home'] = home
        matchup['away'] = away
        matchup['round'] = round
        matchup['start'] = start
        matchup['playoff'] = playoff
        matchup['season'] = season
        self._data = matchup

    def add_playoff_game(self, date='', state=GAME_STATE_SCHEDULED,
                         home_goal=0, away_goal=0, extra_data=None):
        return self.playoff.add_game(self.home, self.away, date, state,
                                     home_goal, away_goal, extra_data)

    def add_season_game(self, date, home_goal, away_goal, extra_data=None):
        return self.season.add_game(self.home, self.away, date,
                                    GAME_STATE_FINISHED, home_goal, away_goal,
                                    extra_data)

    @property
    def winner(self):
        return None

    @property
    def win_games(self):
        if not self.winner:
            return 0
        return self.playoff.home_win + self.playoff.away_win

    @property
    def started(self):
        return False
