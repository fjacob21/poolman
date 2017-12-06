import unittest
from data import PoolDataFactory
from generators import NHLGenerator


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
        t = NHLGenerator(f)
        self.assertTrue(t.generate(2017))


if __name__ == '__main__':
    unittest.main()
