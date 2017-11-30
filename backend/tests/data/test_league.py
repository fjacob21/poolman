import unittest
from data import create_league


class TestLeagueMethods(unittest.TestCase):

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
        league = create_league('nhl', 'National Hockey league',
                               'https://www.nhl.com/')
        league_year = league.add_year(2000)
        self.assertEqual(league.name, 'nhl')
        self.assertEqual(league.desc, 'National Hockey league')
        self.assertEqual(league.website, 'https://www.nhl.com/')
        self.assertEqual(league_year.year, 2000)
        self.assertIsNotNone(league.years[2000])


if __name__ == '__main__':
    unittest.main()
