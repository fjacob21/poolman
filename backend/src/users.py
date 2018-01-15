from data import PowerDict
from data.dateutils import now, date_to_string
from user import User, USER_ACCESS_NORMAL
import hashlib
import random


class Users(PowerDict):

    def __init__(self):
        users = {}
        self._data = users
        self.users = []

    def find(self, username):
        for user in self.users:
            if user.username == username:
                return user
        return None

    def find_by_uid(self, uid):
        for user in self.users:
            if user.uid == uid:
                return user
        return None

    def find_index_by_uid(self, uid):
        for i in range(len(self.users)):
            user = self.users[i]
            if user.uid == uid:
                return i
        return -1

    def find_by_key(self, key):
        for user in self.users:
            if user.login_key == key:
                return user
        return None

    def find_by_email(self, email):
        for user in self.users:
            if user.email == email:
                return user
        return None

    def list(self):
        return self.users

    def generate_id(self):
        hash = hashlib.sha256()
        seed = str(random.getrandbits(20)).encode('utf8')
        idx = str(len(self.users)).encode('utf8')
        hash.update(seed + idx)
        return hash.hexdigest()

    def add(self, username='', access=USER_ACCESS_NORMAL,
            fullname='', email='', phone='', img=None):
        if self.find(username):
            return None
        n = now()
        creation_date = date_to_string(n)
        uid = self.generate_id()
        user = User(uid, username, access, fullname, email,
                    phone, img, creation_date)
        self.users.append(user)
        return user

    def delete(self, uid):
        user_idx = self.find_index_by_uid(uid)
        if user_idx == -1:
            return False
        del self.users[user_idx]
        return True
