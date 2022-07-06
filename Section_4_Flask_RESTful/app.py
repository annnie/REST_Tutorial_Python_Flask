from flask import Flask, request
from flask_restful import Resource, Api
from flask_jwt import JWT, jwt_required

from security import authenticate, identity

app = Flask(__name__)
app.secret_key = 'jan'
api = Api(app)

# JWT json web token
# creates /auth endpoint, this will send username/password and send to authenticate() function
jwt = JWT(app, authenticate, identity)

items = []


class Item(Resource):
    @jwt_required()
    def get(self, name):
        # filter() returns a filter object, can call a number of functions on the response
        # item = list(filter(lambda x : x['name'] ==  name, items))
        # next will return the first item found by the filter function, in ours there will only be one item found
        # adding None is the defualt return
        item = next(filter(lambda x: x['name'] == name, items), None)
        return {'item': item}, 200 if item else 404

    def post(self, name):
        # check if we already added this name to our list, return 400 to indicate user error
        if next(filter(lambda x: x['name'] == name, items), None) is not None:
            return {'message': "An item with nane '{}' already exists".format(name)}, 400

        data = request.get_json()  # can use silent or force as inputs
        price = data['price']
        print('Adding price: ', price, 'for item: ', name)
        item = {'name': name, 'price': price}
        items.append(item)
        return item, 201

    def delete(self, name):
        global items
        items = list(filter(lambda x: x['name'] != name, items))
        return {'message': 'Item deleted'}

    def put(self, name):
        data = request.get_json()
        item = next(filter(lambda x: x['name'] == name, items), None)
        if item is None:
            item = {'name': name, 'price': data['price']}
            items.append(item)
        else:
            item.update(data)
        return item

class ItemList(Resource):
    def get(self):
        return {'items': items}


api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')

app.run(port=5000)
