import flask

from jmd import crypt
from jmd.model import User


class UserObj(object):
    def __init__(self, user_obj=None):
        self._user_obj = user_obj

    @staticmethod
    def get(user_id):
        doc = User.objects(email=user_id).first()
        if doc:
            return UserObj(doc)

    @staticmethod
    def login(user_id, password):
        doc = User.objects(email=user_id).first()
        is_valid = None
        if doc:
            is_valid = crypt.check_password_hash(doc['password'], password)
        if is_valid:
            user = UserObj(doc)
            user.authenticated = True
            return user

    @staticmethod
    def create(user_id, password):
        hash = crypt.generate_password_hash(password)
        try:
            User(email=user_id, password=hash).save()
        except Exception as e:
            flask.flash(e.message, 'danger')
        else:
            return True

    def is_authenticated(self):
        return getattr(self, 'authenticated', None)

    def is_active(self):
        return getattr(self._user_obj, 'active', None)

    def is_anonymous(self):
        return False

    def get_id(self):
        return getattr(self._user_obj, 'email', None)
