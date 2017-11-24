import unittest
from data import PoolDataFactory
from generators import NHLStandingGenerator


class TestNHLStandingGeneratorMethods(unittest.TestCase):

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
        f = PoolDataFactory()
        t = NHLStandingGenerator(f, 2017)
        self.assertTrue(t.generate())


if __name__ == '__main__':
    unittest.main()
