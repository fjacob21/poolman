import unittest
from data import PoolDataFactory
from generators import NHLTeamGenerator, NHLGameGenerator


class TestNHLGameGeneratorMethods(unittest.TestCase):

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
        f = PoolDataFactory()
        t = NHLTeamGenerator(f)
        teams = t.generate()
        g = NHLGameGenerator(f, 2017, teams[list(teams.keys())[0]].id)
        self.assertTrue(g.generate())


if __name__ == '__main__':
    unittest.main()
