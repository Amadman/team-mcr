"""Routing functions for Flask."""
import json
from json import loads
import os

from .classes import get_range
from .statistics import get_mean_distance, get_modal_distance

from flask import session, render_template, request, url_for, redirect
from flask_babel import gettext

from app import app, babel, socketio
from config import LANGUAGES

with open(os.path.join(app.root_path, 'static', 'data', 'classes.json')) as f:
    classes = loads(f.read())

@app.route("/")
def index():
    """Index page."""
    return render_template("index.html", title=gettext("Home"),
                           mean_distance=get_mean_distance(classes),
                           modal_distance=get_modal_distance(classes))

@app.route("/about")
def about():
    """About page."""
    return render_template("about.html", title=gettext("About"))

@app.route("/lang/<language>")
def lang(language=None):
     session["language"] = language
     return redirect(url_for("index"))

@babel.localeselector
def get_locale():
    try:
        language = session['language']
    except KeyError:
        language = None
    return language if language else request.accept_languages.best_match(LANGUAGES.keys())

@socketio.on('event')
def on_connect(message):
    """Called when the user connects to the websocket."""
    print('received message: {0}'.format(str(message)))

@socketio.on('update')
def update_x(message):
    """Called when the slider's value is updated."""
    print("update: {0}".format(str(message)))
    print("Getting the required data...")
    start, end = message['data'][0], message['data'][1]
    data = get_range(classes, start, end)
    print("Done! Now sending data...")
    socketio.emit('data', data)
