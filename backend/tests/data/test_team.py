import unittest
from data import create_team


class TestTeamMethods(unittest.TestCase):

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
        leagueinfo = {'league': 'testleague'}
        team = create_team(1, 'TAM', 'Team', 'Test team',
                           'City', True, 1900, 'http://tam.com')
        team.set_venue('City', 'City venue', 'America/New_York', '123 street')
        team.league_info = leagueinfo
        self.assertEqual(team.id, 1)
        self.assertEqual(team.abbreviation, 'TAM')
        self.assertEqual(team.name, 'Team')
        self.assertEqual(team.fullname, 'Test team')
        self.assertEqual(team.city, 'City')
        self.assertEqual(team.active, True)
        self.assertEqual(team.creation_year, 1900)
        self.assertEqual(team.website, 'http://tam.com')
        self.assertEqual(team.venue.city, 'City')
        self.assertEqual(team.venue.name, 'City venue')
        self.assertEqual(team.venue.timezone, 'America/New_York')
        self.assertEqual(team.venue.address, '123 street')
        self.assertEqual(team.league_info['league'], 'testleague')


if __name__ == '__main__':
    unittest.main()
