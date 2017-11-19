import unittest
from data import PoolDataFactory
from generators import NHLMatchupTreeGenerator


class TestNHLTreeGeneratorMethods(unittest.TestCase):

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
        f = PoolDataFactory()
        t = NHLMatchupTreeGenerator(f, 2017)
        self.assertTrue(t.generate())


if __name__ == '__main__':
    unittest.main()
