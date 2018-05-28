from flask_restful import Resource, reqparse
import sqlite3


class User:
    def __init__(self, _id, username, password):
        self.id = _id
        self.username = username
        self.password = password

    @classmethod
    def find_by_username(cls, username):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "SELECT * FROM users WHERE username=?"
        result = cursor.execute(query, (username,))
        row = result.fetchone()  # get the first result

        if row is not None:
            # user = cls(row[0],row[1],row[2])
            user = cls(*row)
        else:
            user = None

        connection.close()

        return user

    @classmethod
    def find_by_id(cls, _id):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "SELECT * FROM users WHERE id=?"
        result = cursor.execute(query, (_id,))
        row = result.fetchone()  # get the first result

        if row is not None:
            # user = cls(row[0],row[1],row[2])
            user = cls(*row)
        else:
            user = None

        connection.close()

        return user


class UserRegister(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('username', type=str, required=True,
                        help='this field cannot be left blank!')
    parser.add_argument('password', type=str, required=True,
                        help='this field cannot be left blank!')

    def post(self):
        # check incomming data for valid register
        data = UserRegister.parser.parse_args()

        # check if username already exist
        check_user = User.find_by_username(data['username'])
        if check_user:
            return {"message": "This username already exist"}, 400

        # Create connection
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "INSERT INTO users VALUES (NULL, ?, ?)"
        cursor.execute(query, (data['username'], data['password']))

        connection.commit()

        connection.close()

        return {"message": "Your New user was created!"}, 201
