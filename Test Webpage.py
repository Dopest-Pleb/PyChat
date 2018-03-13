from flask import Flask, render_template
from flask_socketio import SocketIO, send, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('test.html')

@socketio.on('send_message')
def handle_message(message):
    emit('message', message)

if __name__ == '__main__':
    socketio.run(app)
