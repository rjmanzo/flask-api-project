from flask import Flask, request
from flask_restful import Resource, Api, reqparse
import local_settings

app = Flask(__name__)
app.secret_key = '01245552357SDGKSDHSDGSDG352NKSGSSDS75'
api = Api(app)

items = []


class Item(Resource):

    # we define the request argument at top. POST & PUT need the same data
    parser = reqparse.RequestParser()
    parser.add_argument(
        'price',
        type=float,
        required=True,
        help='this field cannot be left blank!'
    )

    def get(self, name):
        # for item in items:
        #     if item['name'] == name:
        #         return item
        # next grab one item (pop List) each time.
        item = next(filter(lambda x: x['name'] == name, items), None)
        return {'items': item}, 200 if item is not None else 404

    def post(self, name):

        # verify that the name was not taken. If was return a message
        if next(filter(lambda x: x['name'] == name, items), None):
            return {'message': "An item with name '{}' already exist".format(name)}, 400

        # silent=True prevent an error and return null
        #data = request.get_json(silent=True)
        data = Item.parser.parser_arg()

        item = {
            'name': name,
            'price': data['price']
        }

        items.append(item)

    def delete(self, name):
        # when a variable it's filter and be reasign to the same variable you have to set global
        global items
        act_len = len(items)
        items = list(filter(lambda x: x['name'] != name, items))

        if act_len > len(items):
            return {'message': 'the item was deleted!'}, 200
        else:
            return {'message': 'the item was not found!'}, 404

    def put(self, name):

        data = Item.parser.parser_arg()

        item = next(filter(lambda x: x['name'] == name, items), None)

        if item is None:  # if not exist we create the new item
            item = {'name': name, 'price': data['name']}
            items.append(item)
            return item, 201  # return the created item
        else:
            items.update(item)
            return item, 200  # return the updated item


class ItemList(Resource):
    def get(self):
        return {'items': items}


# host:port/student/<string:name>
api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')

# with this syntax you can run the server only with this command : python app.py
app.run(port=5000, debug=True)
# The other option for running the server its to specifice Flask what it's the file to run
# with this command line : FLASK_APP=app.py run flask
