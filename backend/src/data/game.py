from .powerdict import PowerDict

GAME_STATE_SCHEDULED = 1
GAME_STATE_IN_PROGRESS = 2
GAME_STATE_FINISHED = 3


def create_game(home=0, away=0, date='', state=GAME_STATE_SCHEDULED,
                home_goal=0, away_goal=0, extra_data=None):
    return Game(home, away, date, state, home_goal, away_goal,
                extra_data)


class Game(PowerDict):

    def __init__(self, home=0, away=0, date='', state=GAME_STATE_SCHEDULED,
                 home_goal=0, away_goal=0, extra_data=None):
        game = {}
        game['home'] = home
        game['away'] = away
        game['date'] = date
        game['state'] = state
        game['home_goal'] = home_goal
        game['away_goal'] = away_goal
        game['extra_data'] = extra_data
        self._data = game
