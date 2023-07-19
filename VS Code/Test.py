from flask import Flask, jsonify, request

app = Flask(__name__)

cars = [{'Brand': 'Mahindra'}, {'Brand': 'Tata'}, {'Brand': 'MG'}, {'Brand': 'Jeep'}]

@app.route('/', methods=['GET'])
def test():
    return jsonify({'message': 'It works!'})

@app.route('/car', methods=['GET'])
def get_cars():
    return jsonify({'cars': cars})

@app.route('/car/<string:Brand>', methods=['GET'])
def returnOne(Brand):
    car = [car for car in cars if car['Brand'] == Brand]
    return jsonify({'Carz': car[0]})

@app.route('/car', methods=['POST'])
def carONE():
    car = {'Brand': request.json['Brand']}
    cars.append(car)
    return jsonify({'cars': cars})

@app.route('/car/<string:Brand>', methods=['PUT'])
def edit_car(Brand):
    car = [car for car in cars if car['Brand'] == Brand]
    car[0]['Brand'] = request.json['Brand']
    return jsonify({'Carz': car[0]})

@app.route('/car/<string:Brand>', methods=['DELETE'])
def delete_car(Brand):
    car = [car for car in cars if car['Brand'] == Brand]
    cars.remove(car[0])
    return jsonify({'cars': cars})

if __name__ == "__main__":
    app.run(debug=True, port=8080)


