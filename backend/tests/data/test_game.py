import unittest
from data import create_game, GAME_STATE_FINISHED


class TestGameMethods(unittest.TestCase):

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

    def test_game(self):
        extradata = {'penalities': 'test'}
        game = create_game(1, 2, '2017-04-10T00:41:45Z', GAME_STATE_FINISHED,
                           1, 0, extradata)
        self.assertEqual(game.home, 1)
        self.assertEqual(game.away, 2)
        self.assertEqual(game.date, '2017-04-10T00:41:45Z')
        self.assertEqual(game.state, GAME_STATE_FINISHED)
        self.assertEqual(game.home_goal, 1)
        self.assertEqual(game.away_goal, 0)
        self.assertEqual(game.extra_data['penalities'], 'test')


if __name__ == '__main__':
    unittest.main()
