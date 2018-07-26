"""Routing functions for Flask."""
import json
import os

from flask import render_template
from app import app, socketio

@app.route("/")
def index():
    """Index page."""
    return render_template("index.html", title="Home")

@socketio.on('event')
def on_connect(message):
    """Called when the user connects to the websocket."""
    print('received message: {0}'.format(str(message)))

@socketio.on('update')
def update_x(message):
    """Called when the slider's value is updated."""
    print('update: {0}'.format(str(message)))
    with open(os.path.join(app.root_path, 'static', 'data',
                           'new_schools.json')) as fil:
        data = json.load(fil)
    socketio.emit('data', data)
