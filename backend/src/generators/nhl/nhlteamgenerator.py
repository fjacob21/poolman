import requests


class NHLTeamGenerator(object):

    def __init__(self, factory):
        self._factory = factory

    def generate(self):
        return self.get_teams()

    def extract_team_info(self, team):
        info = {}
        info['id'] = team['id']
        info['abbreviation'] = team['abbreviation']
        info['name'] = team['teamName']
        info['active'] = team['active']
        info['city'] = team['locationName']
        info['fullname'] = team['name']
        info['creation_year'] = team['firstYearOfPlay']
        info['website'] = team['officialSiteUrl']
        return self._factory.create_team(info['id'], info['abbreviation'], info['name'],
                                         info['fullname'], info['city'],
                                         info['active'], info['creation_year'],
                                         info['website'])

    def create_nhl_team_info(self, conference_id, conference_name, division_id,
                             division_name):
        info = {}
        info['conference'] = {'id': conference_id, 'name': conference_name}
        info['division'] = {'id': division_id, 'name': division_name}
        return info

    def extract_team_venue(self, team):
        venue = {}
        venue['city'] = team['venue']['city']
        venue['name'] = team['venue']['name']
        # venue_timezone = team['venue']['timeZone']['id']
        return venue

    def extract_team_league_info(self, team):
        conference_id = team['conference']['id']
        conference_name = team['conference']['name']
        division_id = team['division']['id']
        division_name = team['division']['name']
        return self.create_nhl_team_info(conference_id, conference_name,
                                         division_id, division_name)

    def get_teams(self):
        url = 'https://statsapi.web.nhl.com/api/v1/teams/'
        teams = requests.get(url).json()
        db_teams = {}
        for team in teams['teams']:
            db_team = self.extract_team_info(team)
            venu = self.extract_team_venue(team)
            league_info = self.extract_team_league_info(team)
            db_team.set_venue(venu['city'], venu['name'])
            db_team.league_info = league_info
            db_teams[db_team.id] = db_team
        return db_teams
