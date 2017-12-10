from .nhlteamgenerator import NHLTeamGenerator
from .nhlmatchuptreegenerator import NHLMatchupTreeGenerator
from .nhlmatchuptreeupdater import NHLMatchupTreeUpdater
from .nhlstandinggenerator import NHLStandingGenerator
from .nhlgamegenerator import NHLGameGenerator


class NHLGenerator(object):

    def __init__(self, factory, league=None):
        self._factory = factory
        if not league:
            league = self._factory.create_league('nhl',
                                                 'National Hockey league',
                                                 'https://www.nhl.com/')
        self._league = league

    def generate(self, year):
        self.update_teams()
        if year not in self._league.years:
            league_year = self._league.add_year(year)
            self.generate_year_info(year)
        self.update_year_info(year)
        return self._league

    def update_teams(self):
        if self._league.teams is None:
            t = NHLTeamGenerator(self._factory)
            self._league.teams = t.generate()

    def build_teams_games(self, year):
        league_year = self._league.years[year]
        for standing in league_year.standings.values():
            g = NHLGameGenerator(self._factory, year, standing.team_id)
            g.season_only()
            league_year.teams_games[standing.team_id] = g.generate()

    def update_year_info(self, year):
        league_year = self._league.years[year]
        if league_year.is_year_finished:
            u = NHLMatchupTreeUpdater(self._factory,
                                      year,
                                      league_year.standings,
                                      league_year.matchups)
            league_year.matchups = u.update()
            while u.updated:
                league_year.matchups = u.update()

    def generate_year_info(self, year):
        league_year = self._league.years[year]
        if not league_year.is_year_finished:
            s = NHLStandingGenerator(self._factory, year)
            league_year.standings = s.generate()
            t = NHLMatchupTreeGenerator(self._factory, year,
                                        self._league.teams,
                                        league_year.standings)
            league_year.matchups = t.generate()
            if league_year.is_year_finished:
                self.build_teams_games(year)
