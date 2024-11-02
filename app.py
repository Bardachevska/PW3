from flask import Flask, jsonify, request
app = Flask(__name__)
# Інформативна база даних
stores = []

# Створення магазининів 
@app.route('/store', methods=['POST'])
def create_store():
    request_data = request.get_json()
    new_store = {
        'name': request_data['name'],
        'items': []
    }
    stores.append(new_store)
    return jsonify(new_store), 201

# Додавання товару до магазину
@app.route('/store/<string:name>/item', methods=['POST'])
def create_item_in_store(name):
    request_data = request.get_json()
    for store in stores:
        if store['name'] == name:
            new_item = {
                'name': request_data['name'],
                'price': request_data['price']
            }
            store['items'].append(new_item)
            return jsonify(new_item), 201
    return jsonify({'message': 'Store not found'}), 404

# Отримання магазинів та їх товарів
@app.route('/store', methods=['GET'])
def get_stores():
    return jsonify({'stores': stores})

# Приймання товару в конкретному магазині
@app.route('/store/<string:name>', methods=['GET'])
def get_store(name):
    for store in stores:
        if store['name'] == name:
            return jsonify(store)
    return jsonify({'message': 'Store not found'}), 404

# Отримання лише товарів конкретного магазину
@app.route('/store/<string:name>/item', methods=['GET'])
def get_items_in_store(name):
    for store in stores:
        if store['name'] == name:
            return jsonify(store['items'])
    return jsonify({'message': 'Store not found'}), 404
if __name__ == '__main__':
    app.run(port=5000, debug=True)
