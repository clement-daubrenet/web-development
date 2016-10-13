from flask import Flask
from flask_pymongo import PyMongo


app = Flask(__name__)
mongo = PyMongo(app)

@app.route('/uploads/<path:filename>', methods=['POST'])
def save_upload(filename):
    mongo.save_file(filename, request.files['file'])
    return redirect(url_for('get_upload', filename=filename))

if __name__ == "__main__":
    app.run(debug=True)
