from flask import Flask 
from flask_restful import Api, Resource, abort

app = Flask(__name__)
api = Api(app)

name_dictionary = {"Momo": "23",
                   "Tish": "28"}

class Irish(Resource):
    def get(self, name):
        """
        Get age of an irish girl name
        :name: her name
        """
        try:
            age = name_dictionary[name]
        except KeyError as e:
            abort(404)
        return name_dictionary[name]

api.add_resource(Irish, '/irish/<name>')

if __name__ == "__main__":
    app.run(debug=True) 
