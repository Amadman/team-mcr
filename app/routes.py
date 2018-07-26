"""Routing functions for Flask."""
import json
import os

from app import app, socketio
from flask import render_template

@app.route("/")
def index():
    """Index page."""
    return render_template("index.html", title="Home")

@socketio.on('event')
def on_connect(message):
  print('received message: {0}'.format(str(message)))

@socketio.on('update')
def update_x(message):
  print('update: {0}'.format(str(message)))
  with open(os.path.join(app.root_path, 'static', 'data', 'new_schools.json')) as f:
    data = json.load(f)
  socketio.emit('data', data)
