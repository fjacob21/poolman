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
        pass

    def tearDown(self):
        pass

    def test_team(self):
        m1 = create_matchup('m1', 1, 1, 2, '2017-04-10T00:41:45Z')
        extra_data = {'test': 'test'}
        gs = m1.add_season_game('2017-04-10T00:41:45Z', 1, 0, extra_data)
        gp = m1.add_playoff_game('2017-04-10T00:41:45Z', GAME_STATE_FINISHED,
                                 1, 0, extra_data)
        self.assertEqual(m1.id, 'm1')
        self.assertEqual(m1.home, 1)
        self.assertEqual(m1.away, 2)
        self.assertEqual(m1.round, 1)
        self.assertEqual(m1.start, '2017-04-10T00:41:45Z')
        self.assertIsNotNone(m1.season.games[1])
        self.assertIsNotNone(gs.home, 1)
        self.assertIsNotNone(gs.away, 2)
        self.assertIsNotNone(gs.date, '2017-04-10T00:41:45Z')
        self.assertIsNotNone(gs.state, GAME_STATE_FINISHED)
        self.assertIsNotNone(gs.home_goal, 1)
        self.assertIsNotNone(gs.away_goal, 2)
        self.assertIsNotNone(gs.extra_data['test'], 'test')
        self.assertIsNotNone(m1.playoff.games[1])
        self.assertIsNotNone(gp.home, 1)
        self.assertIsNotNone(gp.away, 2)
        self.assertIsNotNone(gp.date, '2017-04-10T00:41:45Z')
        self.assertIsNotNone(gp.state, GAME_STATE_FINISHED)
        self.assertIsNotNone(gp.home_goal, 1)
        self.assertIsNotNone(gp.away_goal, 2)
        self.assertIsNotNone(gp.extra_data['test'], 'test')


if __name__ == '__main__':
    unittest.main()
