from flask import Flask
from flask_pymongo import PyMongo
from bson.json_util import dumps
from bson.objectid import ObjectId
from flask import request
from flask import jsonify, request
from werkzeug.security import  generate_password_hash,check_password_hash


app = Flask(__name__)
app.secret_key = "secretkey"
app.config["MONGO_URI"] = "mongodb://localhost:27017/testDB"
mongo = PyMongo(app)

@app.route('/add', methods=['POST'])
def add_user():
    _json = request.json
    _name = _json['name']
    _email = _json['email']
   

    if _name and _email and request.method == 'POST':
        id = mongo.db.users.insert({'name': _name,
                                   'email': _email
                                   
        })

        response = jsonify("Successfull")

        response.status_code = 200
        return response
    else:
        return not_found()
        
@app.errorhandler(404)
def not_found(error=None):
    message = {
        'status': 404,
        'message': 'Not Found' + request.url
    }
    response = jsonify(message)
    response.status_code = 404
    return response

if __name__ == "__main__":
    app.run(debug=True)