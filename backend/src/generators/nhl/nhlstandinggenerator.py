import requests


class NHLStandingGenerator(object):

    def __init__(self, factory, year):
        self._factory = factory
        self._year = year

    def generate(self):
        return self.get_standing()

    def create_nhl_ranks(self, league_rank, conference_rank,
                         division_rank, wildCard_rank):
        rank = {}
        rank['league_rank'] = league_rank
        rank['conference_rank'] = conference_rank
        rank['division_rank'] = division_rank
        rank['wildCard_rank'] = wildCard_rank
        return rank

    def extract_standing_info(self, team_standing):
        info = {}
        info['team_id'] = int(team_standing['team']['id'])
        info['pts'] = int(team_standing['points'])
        info['win'] = int(team_standing['leagueRecord']['wins'])
        info['losses'] = int(team_standing['leagueRecord']['losses'])
        info['ot'] = int(team_standing['leagueRecord']['ot'])
        info['games_played'] = int(team_standing['gamesPlayed'])
        info['goals_against'] = int(team_standing['goalsAgainst'])
        info['goals_scored'] = int(team_standing['goalsScored'])
        return info

    def extract_ranks(self, team_standing):
        league_rank = int(team_standing['leagueRank'])
        conference_rank = int(team_standing['conferenceRank'])
        division_rank = int(team_standing['divisionRank'])
        wildCard_rank = int(team_standing['wildCardRank'])
        return self.create_nhl_ranks(league_rank, conference_rank,
                                     division_rank, wildCard_rank)

    def get_standing(self):
        ystr = str(self._year) + str(self._year + 1)
        url = 'https://statsapi.web.nhl.com/api/v1/standings?season=' + ystr
        standing = requests.get(url).json()["records"]
        db_standings = {}
        for division in standing:
            for team_standing in division['teamRecords']:
                info = self.extract_standing_info(team_standing)
                ranks = self.extract_ranks(team_standing)
                standing = self._factory.create_standing(info['team_id'],
                                                         info['pts'],
                                                         info['win'],
                                                         info['losses'],
                                                         info['ot'],
                                                         info['games_played'],
                                                         info['goals_against'],
                                                         info['goals_scored'],
                                                         ranks)
                db_standings[info['team_id']] = standing
        return db_standings
