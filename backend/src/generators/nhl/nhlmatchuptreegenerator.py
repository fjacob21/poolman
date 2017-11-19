from .nhlteamgenerator import NHLTeamGenerator
from .nhlstandinggenerator import NHLStandingGenerator


class NHLMatchupTreeGenerator(object):

    def __init__(self, factory, year):
        self._factory = factory
        self._year = year

    def generate(self):
        return self.get_matchuptree()

    def create_initial_tree(self):
        tree = self._factory.create_matchup_tree()
        tree.create_node('sc', 4, next=None)

        tree.create_node('e', 3, next=tree.sc)
        tree.create_node('w', 3, next=tree.sc)

        tree.create_node('a', 2, next=tree.e)
        tree.create_node('m', 2, next=tree.e)
        tree.create_node('c', 2, next=tree.w)
        tree.create_node('p', 2, next=tree.w)

        tree.create_node('a1', 1, next=tree.a)
        tree.create_node('a2', 1, next=tree.a)
        tree.create_node('m1', 1, next=tree.m)
        tree.create_node('m2', 1, next=tree.m)
        tree.create_node('c1', 1, next=tree.c)
        tree.create_node('c2', 1, next=tree.c)
        tree.create_node('p1', 1, next=tree.p)
        tree.create_node('p2', 1, next=tree.p)

        tree.update_node_links('sc', tree.e, tree.w)

        tree.update_node_links('w', tree.p, tree.c)
        tree.update_node_links('e', tree.m, tree.a)

        tree.update_node_links('c', tree.c2, tree.c1)
        tree.update_node_links('p', tree.p2, tree.p1)
        tree.update_node_links('a', tree.a2, tree.a1)
        tree.update_node_links('m', tree.m2, tree.m1)
        return tree

    def calculate_standing(self):
        db_standings = {'Eastern': {'Atlantic': [], 'Metropolitan': [],
                        'teams': []}, 'Western': {'Central': [], 'Pacific': [],
                        'teams': []}, 'teams': []}

        league = sorted(self._standing.values(), key=lambda k: int(k.ranks['division_rank']))
        for team in league:
            db_standings['teams'].append(team)
            id = team.team_id
            team_info = self._teams[id]
            db_standings[team_info.league_info['conference']['name']]['teams'].append(team)
            db_standings[team_info.league_info['conference']['name']][team_info.league_info['division']['name']].append(team)
        db_standings['teams'] = sorted(db_standings['teams'], key=lambda k: int(k.ranks['league_rank']))

        db_standings['Eastern']['teams'] = sorted(db_standings['Eastern']['teams'], key=lambda k: int(k.ranks['conference_rank']))
        db_standings['Western']['teams'] = sorted(db_standings['Western']['teams'], key=lambda k: int(k.ranks['conference_rank']))

        db_standings['Eastern']['Atlantic'] = sorted(db_standings['Eastern']['Atlantic'], key=lambda k: int(k.ranks['division_rank']))
        db_standings['Eastern']['Metropolitan'] = sorted(db_standings['Eastern']['Metropolitan'], key=lambda k: int(k.ranks['division_rank']))
        db_standings['Western']['Central'] = sorted(db_standings['Western']['Central'], key=lambda k: int(k.ranks['division_rank']))
        db_standings['Western']['Pacific'] = sorted(db_standings['Western']['Pacific'], key=lambda k: int(k.ranks['division_rank']))
        return db_standings

    def calculate_initial_tree(self):
        ealeader = self._nhlstanding['Eastern']['Atlantic'][0]
        emleader = self._nhlstanding['Eastern']['Metropolitan'][0]
        wcleader = self._nhlstanding['Western']['Central'][0]
        wpleader = self._nhlstanding['Western']['Pacific'][0]
        for team in self._nhlstanding['Eastern']['teams']:
            if int(team.ranks['wildCard_rank']) == 1:
                e1wild = team
            if int(team.ranks['wildCard_rank']) == 2:
                e2wild = team

        for team in self._nhlstanding['Western']['teams']:
            if int(team.ranks['wildCard_rank']) == 1:
                w1wild = team
            if int(team.ranks['wildCard_rank']) == 2:
                w2wild = team

        if int(ealeader.ranks['conference_rank']) < int(emleader.ranks['conference_rank']):
            self._tree.a1['matchup'] = self._factory.create_matchup('a1', 1, ealeader.team_id, e2wild.team_id)
            self._tree.m1['matchup'] = self._factory.create_matchup('m1', 1, emleader.team_id, e1wild.team_id)
        else:
            self._tree.a1['matchup'] = self._factory.create_matchup('a1', 1, ealeader.team_id, e1wild.team_id)
            self._tree.m1['matchup'] = self._factory.create_matchup('m1', 1, emleader.team_id, e2wild.team_id)

        self._tree.a2['matchup'] = self._factory.create_matchup('a2', 1, self._nhlstanding['Eastern']['Atlantic'][1].team_id, self._nhlstanding['Eastern']['Atlantic'][2].team_id)
        self._tree.m2['matchup'] = self._factory.create_matchup('m2', 1, self._nhlstanding['Eastern']['Metropolitan'][1].team_id, self._nhlstanding['Eastern']['Metropolitan'][2].team_id)


        if int(wcleader.ranks['conference_rank']) < int(wpleader.ranks['conference_rank']):
            self._tree.c1['matchup'] =self._factory.create_matchup('c1', 1, wcleader.team_id, w2wild.team_id)
            self._tree.p1['matchup'] = self._factory.create_matchup('p1', 1, wpleader.team_id, w1wild.team_id)
        else:
            self._tree.c1['matchup'] = self._factory.create_matchup('c1', 1, wcleader.team_id, w1wild.team_id)
            self._tree.p1['matchup'] = self._factory.create_matchup('p1', 1, wpleader.team_id, w2wild.team_id)

        self._tree.c2['matchup'] = self._factory.create_matchup('c2', 1, self._nhlstanding['Western']['Central'][1].team_id, self._nhlstanding['Western']['Central'][2].team_id)
        self._tree.p2['matchup'] = self._factory.create_matchup('p2', 1, self._nhlstanding['Western']['Pacific'][1].team_id, self._nhlstanding['Western']['Pacific'][2].team_id)

    def get_matchuptree(self):
        t = NHLTeamGenerator(self._factory)
        self._teams = t.generate()
        s = NHLStandingGenerator(self._factory, self._year)
        self._standing = s.generate()

        self._tree = self.create_initial_tree()
        self._nhlstanding = self.calculate_standing()
        self.calculate_initial_tree()

        return self._tree
