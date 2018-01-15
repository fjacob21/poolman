from data import PowerDict
from data.dateutils import now, date_to_string
import hashlib

DEFAULT_SALT = 'superhero'

USER_ACCESS_NORMAL = 0x0
USER_ACCESS_ADMIN = 0x1


class User(PowerDict):

    def __init__(self, uid='', username='', psw='', access=USER_ACCESS_NORMAL,
                 fullname='', email='', phone='', img=None, creation_date=''):
        user = {}
        self._data = user
        self.uid = uid
        self.change_username(username)
        self.change_psw(psw)
        self.access = access
        self.change_info(fullname, email, phone)
        self.change_img(img)
        self.creation_date = creation_date
        self.last_login = ''
        self.login_key = ''

    def login(self, psw):
        if not self.pswcheck(psw):
            return ''
        self.last_login = date_to_string(now())
        self.login_key = self.generate_hash(self.last_login)
        return self.login_key

    def logout(self):
        if not self.login_key:
            return False
        self.login_key = ''
        return True

    def change_info(self, fullname=None, email=None, phone=None):
        if fullname:
            self.fullname = fullname
        if email:
            self.email = email
        if phone:
            self.phone = phone

    def change_username(self, new_username):
        self.username = new_username

    def change_img(self, new_img):
        self.img = new_img

    def change_psw(self, new_psw):
        self.psw = self.generate_hash(new_psw)

    def generate_hash(self, value, salt=DEFAULT_SALT):
        hash = hashlib.sha256()
        h = salt.encode('utf8') + self.uid.encode('utf8')
        h += value.encode('utf8')
        hash.update(h)
        return hash.hexdigest()

    def pswcheck(self, psw):
        hpsw = self.generate_hash(psw)
        return hpsw == self.psw
