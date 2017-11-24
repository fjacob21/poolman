import unittest
from data import create_standing


class TestStandingMethods(unittest.TestCase):

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

    def test_standing(self):
        ranks = {'league': 1}
        extrainfo = {'info': 'info'}
        standing = create_standing(1, 100, 50, 25, 25, 100, 500, 1000,
                                   ranks, extrainfo)
        self.assertEqual(standing.team_id, 1)
        self.assertEqual(standing.pts, 100)
        self.assertEqual(standing.win, 50)
        self.assertEqual(standing.losses, 25)
        self.assertEqual(standing.ot, 25)
        self.assertEqual(standing.games_played, 100)
        self.assertEqual(standing.goals_against, 500)
        self.assertEqual(standing.goals_scored, 1000)
        self.assertEqual(standing.ranks['league'], 1)
        self.assertEqual(standing.extra_info['info'], 'info')


if __name__ == '__main__':
    unittest.main()
