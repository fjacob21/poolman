from .nhlgamegenerator import NHLGameGenerator


class NHLMatchupTreeUpdater(object):

    def __init__(self, factory, year, standings, tree):
        self._factory = factory
        self._year = year
        self._tree = tree
        self._standings = standings
        self._updated = False

    @property
    def updated(self):
        return self._updated

    def update_matchup(self, node):
        matchup = node.matchup
        g = NHLGameGenerator(self._factory, self._year, matchup.home)
        g.playoff_only()
        games = g.generate()
        self._updated = False
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
            self._updated = True
            next = self._tree[node.next]
            if not next.matchup:
                next.matchup = self._factory.create_matchup(next.id, node.round + 1, matchup.winner)
            else:
                next.matchup.away = matchup.winner
                # Need to order teams!!!!!!!
                home = self._standings[next.matchup.home]
                away = self._standings[next.matchup.away]
                if away.ranks['conference_rank'] < home.ranks['conference_rank']:
                    t = next.matchup.home
                    next.matchup.home = next.matchup.away
                    next.matchup.away = t

    def update(self):
        for node in self._tree.data.values():
            if node.matchup and node.state != self._factory.STATE_FINISHED:
                self.update_matchup(node)
        return self._tree
