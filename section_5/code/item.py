import sqlite3
from flask_restful import Resource, Api, reqparse
from flask_jwt import jwt_required


class Item(Resource):
    # we define the request argument at top. POST & PUT need the same data
    parser = reqparse.RequestParser()
    parser.add_argument('price', type=float, required=True,
                        help='this field cannot be left blank!')

    @classmethod
    def find_by_name(cls, name):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "SELECT * FROM items where name=?"

        result = cursor.execute(query, (name,))
        row = result.fetchone()
        connection.close()

        if row:
            return {"item": {"name": row[0], "price": row[1]}}

        return None

    @jwt_required()
    def get(self, name):

        item = Item.find_by_name(name)  # check if item exist

        if item is not None:
            return item, 200

        # if item dont exists
        return {"message": "item not found"}, 404

    # @jwt_required
    def post(self, name):
        # verify that the name was not taken. If was return a message
        if Item.find_by_name(name) is not None:
            return {'message': "An item with name '{}' already exist".format(name)}, 400

        data = Item.parser.parse_args()

        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "INSERT INTO items values (?, ?)"
        result = cursor.execute(query, (name, data['price']))
        connection.commit()
        connection.close()

        # return the created item
        return {"item": {"name": name, "price": data['price']}}, 201

    def delete(self, name):

        if Item.find_by_name(name) is not None:
            return {'message': "The item {} does not exist".format(name)}, 400

        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "DELETE * FROM items WHERE name = ?"
        result = cursor.execute(query, (name,))

        return {'message': 'the item was deleted!'}, 200

    # @jwt_required
    def put(self, name):

        data = Item.parser.parse_args()

        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        # verify that the name was not taken. If was return a message
        if Item.find_by_name(name) is not None:

            query = "INSERT INTO items values (?, ?)"
            result = cursor.execute(query, (name, data['price']))
            connection.commit()
            connection.close()

            # return the created item
            return {"item": {"name": name, "price": data['price']}}, 201

        else:

            query = "UPDATE items SET name = ?, price = ? WHERE name = ?"
            result = cursor.execute(query, (name, data['price'], name))
            connection.commit()
            connection.close()

            # Update the item
            return {"message": "Item updated!"}, 200


class ItemList(Resource):

    def get(self):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        items = []
        query = "SELECT * FROM items"
        result = cursor.execute(query)
        # fetch all item and insert into items
        for row in result:
            items.append({'name': row[0], 'price': row[1]})

        connection.close()

        return {'items': items}
