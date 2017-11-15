from .team import create_team
from .game import create_game, GAME_STATE_SCHEDULED, GAME_STATE_IN_PROGRESS
from .game import GAME_STATE_FINISHED


class PoolDataFactory(object):

    def __init__(self):
        self.GAME_STATE_SCHEDULED = GAME_STATE_SCHEDULED
        self.GAME_STATE_IN_PROGRESS = GAME_STATE_IN_PROGRESS
        self.GAME_STATE_FINISHED = GAME_STATE_FINISHED

    def create_team(self, id=0, abbreviation='', name='', fullname='', city='',
                    active=False, creation_year=0, website='',
                    venue=None, league_info=None):
        return create_team(id, abbreviation, name, fullname, city, active,
                           creation_year, website, venue, league_info)

    def create_game(self, home=0, away=0, date='', state=GAME_STATE_SCHEDULED,
                    home_goal=0, away_goal=0, extra_data=None):
        return create_game(home, away, date, state, home_goal, away_goal,
                           extra_data)
