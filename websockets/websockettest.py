import redis
from flask import Flask, render_template

app = Flask(__name__)
db = redis.StrictRedis('localhost')

@app.route('/')
def main():
   c=db.incr('counter')
   return render_template("main.html", counter=c)

if __name__ == "__main__":
    app.run(debug=True)
