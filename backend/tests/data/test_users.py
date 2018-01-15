import unittest
from users import Users
from user import USER_ACCESS_ADMIN


class TestUsersMethods(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        self.users = Users()

    def tearDown(self):
        pass

    def add_user(self):
        return self.users.add('test', '12345', USER_ACCESS_ADMIN, 'test',
                              'test@test.com', '555-888-7777')

    def test_add(self):
        user = self.add_user()
        self.assertIsNotNone(user)
        self.assertEqual(len(self.users.list()), 1)
        self.assertEqual(user.username, 'test')
        self.assertEqual(user.access, USER_ACCESS_ADMIN)
        self.assertEqual(user.fullname, 'test')
        self.assertEqual(user.email, 'test@test.com')
        self.assertEqual(user.phone, '555-888-7777')

    def test_delete(self):
        user = self.add_user()
        self.assertFalse(self.users.delete(''))
        self.assertTrue(self.users.delete(user.uid))
        self.assertEqual(len(self.users.list()), 0)

    def test_find(self):
        user = self.add_user()
        self.assertEqual(self.users.find('test'), user)
        self.assertEqual(self.users.find_by_uid(user.uid), user)
        self.assertEqual(self.users.find_by_email('test@test.com'), user)

    def test_login(self):
        user = self.add_user()
        self.assertEqual(user.login(''), '')
        self.assertFalse(user.logout())
        key = user.login('12345')
        self.assertNotEqual(user.last_login, '')
        self.assertNotEqual(key, '')
        self.assertEqual(self.users.find_by_key(key), user)
        self.assertTrue(user.logout())

    def test_change_psw(self):
        user = self.add_user()
        user.change_psw('54321')
        self.assertEqual(user.login('12345'), '')
        key = user.login('54321')
        self.assertNotEqual(key, '')
        self.assertEqual(self.users.find_by_key(key), user)
        self.assertTrue(user.logout())


if __name__ == '__main__':
    unittest.main()
