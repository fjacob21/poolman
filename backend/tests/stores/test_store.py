import unittest
from stores import DB_TYPE_DEBUG, DB_TYPE_PROD, DB_TYPE_TEST
from stores import set_type, release, get


class TestMemoryStoreMethods(unittest.TestCase):

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

    def test_test(self):
        try:
            set_type(DB_TYPE_TEST)
            db = get()
            self.assertIsNotNone(db)
            self.assertIsNotNone(db.connect())
            db.disconnect()
            release()
        except Exception as e:
            self.fail(e)

    def test_debug(self):
        try:
            set_type(DB_TYPE_DEBUG)
            db = get()
            self.assertIsNotNone(db)
            self.assertIsNotNone(db.connect())
            db.disconnect()
            release()
        except Exception as e:
            self.fail(e)

    def test_prod(self):
        try:
            set_type(DB_TYPE_PROD)
            db = get()
            self.assertIsNotNone(db)
            self.assertIsNotNone(db.connect())
            db.disconnect()
            release()
        except Exception as e:
            self.fail(e)


if __name__ == '__main__':
    unittest.main()
