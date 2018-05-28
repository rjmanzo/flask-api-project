from user import User
from werkzeug.security import safe_str_cmp


def authenticate(username, password):
    user = User.find_by_username(username)
    if user and safe_str_cmp(user.password.encode('utf-8'), password.encode('utf-8')):
        return user


def identity(payload):
    user_id = payload['identity']
    # this method get data or return None
    return User.find_by_id(user_id)
