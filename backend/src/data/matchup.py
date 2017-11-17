from .game import create_game, GAME_STATE_SCHEDULED, GAME_STATE_FINISHED
from .matchupresult import MatchupResult
from .powerdict import PowerDict


def create_matchup(id=0, round=0, home=0, away=0, start='',
                   playoff=MatchupResult(), season=MatchupResult()):
    return Matchup(id, round, home, away, start, playoff, season)


class Matchup(PowerDict):

    def __init__(self, id=0, round=0, home=0, away=0, start='',
                 playoff=MatchupResult(), season=MatchupResult()):
        matchup = {}
        matchup['id'] = id
        matchup['home'] = home
        matchup['away'] = away
        matchup['round'] = round
        matchup['start'] = start
        matchup['playoff'] = playoff
        matchup['season'] = season
        self._data = matchup

    def add_playoff_game(self, date='', state=GAME_STATE_SCHEDULED,
                         home_goal=0, away_goal=0, extra_data=None):
        game = create_game(self.home, self.away, date, state, home_goal,
                           away_goal, extra_data)
        self.playoff.games.append(game)
        return game

    def add_season_game(self, date, home_goal, away_goal, extra_data=None):
        game = create_game(self.home, self.away, date, GAME_STATE_FINISHED,
                           home_goal, away_goal, extra_data)
        self.season.games.append(game)
        return game

    @property
    def started(self):
        return False
