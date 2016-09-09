import redis
from flask import Flask, render_template
from flask.ext.socketio import SocketIO
from gevent import monkey
monkey.patch_all()

app = Flask(__name__)
db = redis.StrictRedis('localhost')
socketio = SocketIO(app) 

@app.route('/')
def main():
   c=db.incr('counter')
   return render_template("main.html", counter=c)

@socketio.on("connect",namespace="/connexions")
def ws_connect():
    c = db.incr('connected')
    socketio.emit('msg', {'counter': c}, namespace="/connexions")

@socketio.on("disconnect",namespace="/connexions")
def ws_disconnect():
    c = db.decr('connected')
    socketio.emit('msg', {'counter': c}, namespace="/connexions")

if __name__ == "__main__":
    socketio.run(app)
