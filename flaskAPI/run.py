from flask import Flask, request, jsonify, make_response
from flask_restful import Resource, Api

app = Flask("__name__")
api = Api(app)

cart = []

class Cart(Resource):
   def get(self):
       return make_response(jsonify({'Cart_Items': cart}), 200)

   def post(self):
       data = request.get_json()
       id = len(cart) + 1
       name = data['name']
       price = data['price']
       item = {'id': id, 'name': name, "price": price}
       cart.append(item)
       return make_response(jsonify({'Cart_Items': cart}), 201)

class SingleOrder(Resource):
    def get(self, itemID):
        # for item in cart:
        #     if item['id'] == itemID:
        #         return make_response(jsonify({'Item': item}), 200)

        item = [item for item in cart if item['id'] == itemID]
        if item:
            return make_response(jsonify({'Item': item}), 200)

api.add_resource(Cart, '/')
api.add_resource(SingleOrder, '/<int:itemID>')

if __name__ == "__main__":
   app.run(debug=True)