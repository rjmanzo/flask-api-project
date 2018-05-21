from user import User
import local_settings

users = [

    User(1, 'bob', '1234')

]

# username mapping --> {'username': { User} }
username_mapping = {user.username: user for user in users}

# userid mapping --> {'userid': { User} }
userid_mapping = {user.id: user for user in users}


def authenticate(username, password):
    user = username_mapping.get(username, None)
    if user and user.password == password
        return user


def identity(payload):
    user_id = payload['identity']
    # this method get data or return None
    return userid_mapping.get(user_id, None)


# EXAMPLES

#  users = [
#     {
#         'id': 1,
#         'username': 'bob',
#         'password': '1234'
#     }
# ]

# username_mapping = {
#     'bob': {

#         'id': 1,
#         'username': 'bob',
#         'password': '1234'
#     }
# }

# userid_mapping = {
#     1: {

#         'id': 1,
#         'username': 'bob',
#         'password': '1234'
#     }
# }
