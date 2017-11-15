from .team import create_team


class PoolDataFactory(object):

    def __init__(self):
        pass

    def create_team(seld, id=0, abbreviation='', name='', fullname='', city='',
                    active=False, creation_year=0, website='',
                    venue=None, league_info=None):
        return create_team(id, abbreviation, name, fullname, city, active,
                           creation_year, website, venue, league_info)
