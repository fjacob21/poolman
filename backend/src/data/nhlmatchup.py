from .matchup import Matchup


class NHLMatchup(Matchup):

    def __init__(self, mid=0, round=0, home=0, away=0, start='',
                 playoff=None, season=None):
        Matchup.__init__(self, mid, round, home, away, start, playoff, season)

    @property
    def winner(self):
        if self.playoff.home_win == 4:
            return self.home
        if self.playoff.away_win == 4:
            return self.away
        return None
