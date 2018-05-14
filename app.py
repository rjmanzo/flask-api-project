from flask import Flask, jsonify, request

app = Flask(__name__)

stores = [
    {
        'name': 'the_store',
        'items': [
            {
                'name': 'item1',
                'price': 9.5
            }
        ]
    }
]

# this method find de store name within the stores list


def find_store(name):
    for store in stores
        if store['name'] == name
            return True
    return False


# POST /store data : {name:}
@app.route("/store", methods=["POST"])
def create_store():
    request_data = request.get_json()
    new_store = {
        "name": request_data['name'],
        "items": []
    }
    stores.append(stores)  # append the new store to stores

    # if all was good return the new store list
    return jsonify({"stores": stores})


# GET /store
@app.route("/store")
def get_stores():
    return jsonify({"stores": stores})

# GET  /store/<string: name >


@app.route("/store/<string:name>")
def get_store(name):
    for store in stores:
        if store['name'] == name
            return jsonify(store)  # if store name match then return the store
    return jsonify({'message': 'Store not found!'})

# POST /store/<string:name>/item {name:, price:}


@app.route("/store/<string:name>/item", methods=["POST"])
def create_store_item(name):
    for store in stores:
        request_data = request.get_json()
        new_store_item = {'name': request_data['name'],
                          'price': request_data['price']}
        store['items'].append(new_store_item)  # save new item
        return jsonify(store)  # return updated store

    return jsonify({'message': 'Sorry. Store not found!'})

# GET  /store/<string: name > /item


@app.route("/store/<string:name>/item")
def get_store_item(name, item):
    for store in stores:
        if store['name'] == name
        # if store name match then return the store items
            return jsonify({'items': store['items']})
    return jsonify({'message': 'Store not found!'})
