import unittest
from stores import postgres_store


class TestPostgresStoreMethods(unittest.TestCase):

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

    def test_store(self):
        db = postgres_store('postgres', 'postgres',
                            'mysecretpassword',
                            '192.168.2.99', 5432)
        self.assertIsNotNone(db)
        self.assertIsNotNone(db.connect())
        self.assertFalse(db.table_exist('test'))
        self.assertFalse(db.row_exist('test', 'test'))
        self.assertTrue(db.create_table('test'))
        self.assertTrue(db.create_row('test', 'test', 'test'))
        self.assertIsNotNone(db.get_rows_id('test'))
        self.assertTrue(db.store('test', 'test2', 'test2'))
        self.assertIsNotNone(db.restore('test', 'test'))
        backup = db.backup()
        self.assertIsNotNone(backup)
        self.assertTrue(db.restore_backup(backup))
        self.assertTrue(db.drop_table('test'))
        db.disconnect()

    def test_get_debug(self):
        try:
            db = postgres_store.get_debug()
            self.assertIsNotNone(db)
            self.assertIsNotNone(db.connect())
            db.disconnect()
            postgres_store.release()
        except Exception as e:
            self.fail(e)


if __name__ == '__main__':
    unittest.main()
