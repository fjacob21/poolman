from .nhlgamegenerator import NHLGameGenerator


class NHLMatchupTreeUpdater(object):

    def __init__(self, factory, year, standings, tree):
        self._factory = factory
        self._year = year
        self._tree = tree
        self._standings = standings

    def update_matchup(self, node):
        matchup = node.matchup
        g = NHLGameGenerator(self._factory, 2016, matchup.home)
        g.playoff_only()
        games = g.generate()
        for game in games:
            if ((game.home == matchup.home) and (game.away == matchup.away) or
               (game.home == matchup.away) and (game.away == matchup.home)):
                if not matchup.playoff.find_game(game.date):
                    if matchup.home == game.home:
                        matchup.playoff.add_game(matchup.home, matchup.away, game.date, game.state, game.home_goal, game.away_goal, game.extra_data)
                    else:
                        matchup.playoff.add_game(matchup.home, matchup.away, game.date, game.state, game.away_goal, game.home_goal, game.extra_data)

        if matchup.winner:
            node.state = self._factory.STATE_FINISHED
            if not node.next:
                return
            if not node.next.matchup:
                node.next.matchup = self._factory.create_matchup(node.next.id, node.round + 1, matchup.winner)
            else:
                node.next.matchup.away = matchup.winner
                # Need to order teams!!!!!!!
                home = self._standings[node.next.matchup.home]
                away = self._standings[node.next.matchup.away]
                if away.ranks['conference_rank'] < home.ranks['conference_rank']:
                    t = node.next.matchup.home
                    node.next.matchup.home = node.next.matchup.away
                    node.next.matchup.away = t

    def update(self):
        for node in self._tree.data.values():
            if node.matchup and node.state != self._factory.STATE_FINISHED:
                self.update_matchup(node)
        return self._tree
