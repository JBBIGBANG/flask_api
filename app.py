from flask import Flask, jsonify, request
from flask_pymongo import PyMongo
from bson.json_util import dumps
from bson.objectid import ObjectId
from flask import request


app = Flask(__name__)

# app.config['MONGO_DBNAME'] = 'flask'
app.config['MONGO_URI'] = 'mongodb://localhost/mongo_connect_flassk'

mongo = PyMongo(app)

@app.route('/framework', methods=['GET'])
def get_all_frameworks():

    framework = mongo.db.test1 

    output = []

    for q in framework.find():
      output.append({'name' : q['name'], 'language' : q['language']})

    return jsonify({'result' : output})

@app.route('/framework/<name>', methods=['GET'])
def get_one_framework(name):
    framework = mongo.db.test1

    q = framework.find_one({'name' : name})

    if q:
        output = {'name' : q['name'], 'language' : q['language']}
    else:
        output = 'No results found'

    return jsonify({'result' : output})

@app.route('/framework', methods=['POST'])
def add_framework():
    framework = mongo.db.test1

    name = request.json['name']
    language = request.json['language']

    framework_id = framework.insert_one({'name' : name, 'language' : language})
    new_framework = framework.find_one({'_id' : framework_id})

    output = {'name' : new_framework['name'], 'language' : new_framework['language']}

    return jsonify({'result' :output})

if __name__ == '__main__':
    app.run(debug=True)
