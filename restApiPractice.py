from flask import Flask, request, jsonify

app = Flask(__name__)

stuff = [{'Apple' : '1'}, {'Shoes' : '2'}, {'Trees' : '3'}]

@app.route('/', methods=['GET'])
def test():
	return jsonify({'message' : 'It works!'})

@app.route('/stuff', methods=['GET'])
def returnAll():
	return jsonify({'stuff' : stuff})

@app.route('/stuff/<string:name>', methods=['GET'])
def returnOne(name):
	return jsonify({'item' : stuff[name][0]})

@app.route('/stuff', methods=['POST'])
def addOne():
	item = {'item' : request.form['item']}
	stuff.append(item)
	return jsonify({'languages' : stuff})

@app.route('/stuff/<string:name>', methods=['DELETE'])
def removeOne(name):
	stuff.remove(stuff[name][0])
	return jsonify({'stuff' : stuff})

if __name__ == '__main__':
	app.run(debug=True, port=8080)
