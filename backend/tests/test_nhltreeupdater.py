import unittest
from data import PoolDataFactory
from generators import NHLMatchupTreeGenerator, NHLMatchupTreeUpdater
from generators import NHLStandingGenerator


class TestNHLTreeUpdaterMethods(unittest.TestCase):

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

    def test_tree(self):
        year = 2016
        f = PoolDataFactory()
        s = NHLStandingGenerator(f, year)
        standings = s.generate()
        t = NHLMatchupTreeGenerator(f, year)
        tree = t.generate()
        u = NHLMatchupTreeUpdater(f, year, standings, tree)
        self.assertTrue(u.update())


if __name__ == '__main__':
    unittest.main()
