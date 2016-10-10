from flask import Flask
from flask_restful import Resource, Api


# Minimal REST API : 
#  1. defining the app, just like any flask app + api (specific Flask-REST)
#  2. A class deriving from Resource with get/put/post methods
#  3. Add those to routes using add_resource on the api

app = Flask(__name__)
api = Api(app)


class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}


class HelloFrance(Resource):
    def get(self):
        return {'hello': 'France'}

api.add_resource(HelloWorld, '/')
api.add_resource(HelloFrance, '/france')

if __name__ == '__main__':
    app.run(debug=True)
