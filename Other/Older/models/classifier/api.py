from flask import Flask
from flask_restful import Resource, Api
from classifier import *

app = Flask(__name__)
api = Api(app)

class Classifier(Resource):
    def get(self):
        return {
            'products': ['Ice Cream', 'Chocolate', 'Fruit', 'Eggs']
        }
    api.add_resource(Classifier, '/')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
