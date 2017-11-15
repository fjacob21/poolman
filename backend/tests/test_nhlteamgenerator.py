import unittest
from data import PoolDataFactory
from generators import NHLTeamGenerator


class TestNHLTeamGeneratorMethods(unittest.TestCase):

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
        self.assertTrue(t.generate())


if __name__ == '__main__':
    unittest.main()
