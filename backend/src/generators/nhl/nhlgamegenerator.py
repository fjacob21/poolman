import requests


FILTER_ALL = 1
FILTER_SEASON = 2
FILTER_PLAYOFF = 3


class NHLGameGenerator(object):

    def __init__(self, factory, year, team, start='10-01', end='06-29'):
        self._factory = factory
        self._year = year
        self._team = team
        self._start = start
        self._end = end
        self._filter = FILTER_ALL

    def generate(self):
        return self.get_games()
    
    def playoff_only(self):
        self._start = '04-01'
        self._end = '06-29'
        self._filter = FILTER_PLAYOFF
        
    def season_only(self):
        self._start = '10-01'
        self._end = '04-29'
        self._filter = FILTER_SEASON

    def all_game(self):
        self._start = '10-01'
        self._end = '06-29'
        self._filter = FILTER_ALL

    def create_nhl_extra_info(self, content, live):
        info = {}
        info['content'] = content
        info['live'] = live
        return info

    def extract_game_info(self, game):
        statuscode = {}
        statuscode[1] = self._factory.GAME_STATE_SCHEDULED  # 'Scheduled'
        statuscode[2] = self._factory.GAME_STATE_SCHEDULED  # 'Pre-Game'
        statuscode[3] = self._factory.GAME_STATE_IN_PROGRESS  # 'In Progress'
        statuscode[4] = self._factory.GAME_STATE_IN_PROGRESS  # 'In Progress - Critical'
        statuscode[5] = self._factory.GAME_STATE_IN_PROGRESS  # 'Game Over'
        statuscode[6] = self._factory.GAME_STATE_IN_PROGRESS  # 'Final'
        statuscode[7] = self._factory.GAME_STATE_FINISHED  # 'Final'
        home = game['teams']['home']['team']['id']
        home_score = game['teams']['home']['score']
        away = game['teams']['away']['team']['id']
        away_score = game['teams']['away']['score']
        date = game['gameDate']
        status = statuscode[int(game['status']['statusCode'])]
        link = game['link']
        content = game['content']['link']
        extra = self.create_nhl_extra_info(content, link)
        return self._factory.create_game(home, away, date, status, home_score,
                                         away_score, extra)

    def get_games(self):
        if self._filter == FILTER_PLAYOFF:
            url = 'https://statsapi.web.nhl.com/api/v1/schedule?startDate=' + str(self._year+1) + '-' + self._start + '&endDate=' + str(self._year+1) + '-' + self._end + '&expand=schedule.teams,schedule.linescore,schedule.broadcasts,schedule.ticket,schedule.game.content.media.epg&leaderCategories=&site=en_nhlCA&teamId=' + str(self._team)
        else:
            url = 'https://statsapi.web.nhl.com/api/v1/schedule?startDate=' + str(self._year) + '-' + self._start + '&endDate=' + str(self._year+1) + '-' + self._end + '&expand=schedule.teams,schedule.linescore,schedule.broadcasts,schedule.ticket,schedule.game.content.media.epg&leaderCategories=&site=en_nhlCA&teamId=' + str(self._team)
        team_schedule = requests.get(url).json()
        db_games = []
        for date in team_schedule['dates']:
            game_json = date['games'][0]
            game_type = game_json['gameType']
            if (self._filter == FILTER_ALL or
                (self._filter == FILTER_SEASON and game_type == 'S') or
                (self._filter == FILTER_PLAYOFF and game_type == 'P')):
                game = self.extract_game_info(game_json)
                db_games.append(game)
        return db_games
