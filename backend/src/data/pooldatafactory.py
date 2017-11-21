from .team import create_team
from .game import create_game, GAME_STATE_SCHEDULED, GAME_STATE_IN_PROGRESS
from .game import GAME_STATE_FINISHED
from .standing import create_standing
from .matchupresult import MatchupResult
from .matchup import create_matchup
from .matchuptree import create_matchup_tree
from .matchuptreenode import STATE_UNITIALIZED, STATE_NOT_STARTED, STATE_STARTED, STATE_FINISHED


class PoolDataFactory(object):

    def __init__(self):
        self.GAME_STATE_SCHEDULED = GAME_STATE_SCHEDULED
        self.GAME_STATE_IN_PROGRESS = GAME_STATE_IN_PROGRESS
        self.GAME_STATE_FINISHED = GAME_STATE_FINISHED
        
        self.STATE_UNITIALIZED = STATE_UNITIALIZED
        self.STATE_NOT_STARTED = STATE_NOT_STARTED
        self.STATE_STARTED = STATE_STARTED
        self.STATE_FINISHED = STATE_FINISHED

    def create_team(self, id=0, abbreviation='', name='', fullname='', city='',
                    active=False, creation_year=0, website='',
                    venue=None, league_info=None):
        return create_team(id, abbreviation, name, fullname, city, active,
                           creation_year, website, venue, league_info)

    def create_game(self, home=0, away=0, date='', state=GAME_STATE_SCHEDULED,
                    home_goal=0, away_goal=0, extra_data=None):
        return create_game(home, away, date, state, home_goal, away_goal,
                           extra_data)

    def create_standing(self, team_id=0, pts=0, win=0, losses=0, ot=0,
                        games_played=0, goals_against=0, goals_scored=0,
                        ranks=0, extra_info={}):
        return create_standing(team_id, pts, win, losses, ot, games_played,
                               goals_against, goals_scored, ranks, extra_info)

    def create_matchup(self, id=0, round=0, home=0, away=0, start='',
                       playoff=None, season=None):
        return create_matchup(id, round, home, away, start, playoff, season)

    def create_matchup_result(self, home_win=0, away_win=0, games=None):
        return MatchupResult(home_win, away_win, games)

    def create_matchup_tree(self):
        return create_matchup_tree()
