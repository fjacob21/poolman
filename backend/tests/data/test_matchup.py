import unittest
from data import create_matchup, GAME_STATE_FINISHED


class TestMatchupMethods(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        self.m1 = create_matchup('m1', 1, 1, 2, '2017-04-10T00:41:45Z')
        self.extra_data = {'test': 'test'}
        self.gs = self.m1.add_season_game('2017-04-10T00:41:45Z', 1, 0, self.extra_data)
        self.gp = self.m1.add_playoff_game('2017-04-10T00:41:45Z', GAME_STATE_FINISHED,
                                           1, 0, self.extra_data)

    def tearDown(self):
        pass

    def test_matchup(self):

        self.assertEqual(self.m1.id, 'm1')
        self.assertEqual(self.m1.home, 1)
        self.assertEqual(self.m1.away, 2)
        self.assertEqual(self.m1.round, 1)
        self.assertEqual(self.m1.start, '2017-04-10T00:41:45Z')
        self.assertIsNotNone(self.m1.season.games[0])
        self.assertIsNotNone(self.gs.home, 1)
        self.assertIsNotNone(self.gs.away, 2)
        self.assertIsNotNone(self.gs.date, '2017-04-10T00:41:45Z')
        self.assertIsNotNone(self.gs.state, GAME_STATE_FINISHED)
        self.assertIsNotNone(self.gs.home_goal, 1)
        self.assertIsNotNone(self.gs.away_goal, 2)
        self.assertIsNotNone(self.gs.extra_data['test'], 'test')
        self.assertIsNotNone(self.m1.playoff.games[0])
        self.assertIsNotNone(self.gp.home, 1)
        self.assertIsNotNone(self.gp.away, 2)
        self.assertIsNotNone(self.gp.date, '2017-04-10T00:41:45Z')
        self.assertIsNotNone(self.gp.state, GAME_STATE_FINISHED)
        self.assertIsNotNone(self.gp.home_goal, 1)
        self.assertIsNotNone(self.gp.away_goal, 2)
        self.assertIsNotNone(self.gp.extra_data['test'], 'test')

    def test_winner(self):
        self.assertIsNone(self.m1.winner)
        self.m1.add_playoff_game('2017-04-10T00:41:45Z', GAME_STATE_FINISHED,
                                 1, 0, self.extra_data)
        self.m1.add_playoff_game('2017-04-10T00:41:45Z', GAME_STATE_FINISHED,
                                 1, 0, self.extra_data)
        self.m1.add_playoff_game('2017-04-10T00:41:45Z', GAME_STATE_FINISHED,
                                 1, 0, self.extra_data)
        self.assertEqual(self.m1.winner, 1)

    def test_find_game(self):
        self.assertIsNone(self.m1.season.find_game(''))
        self.assertIsNotNone(self.m1.season.find_game('2017-04-10T00:41:45Z'))


if __name__ == '__main__':
    unittest.main()
