"""Routing functions for Flask."""
from json import loads
import os

from flask import session, render_template, request, url_for, redirect
from flask_babel import gettext

from app import app, babel, socketio
from config import LANGUAGES

from .classes import get_range
from .statistics import get_mean_distance, get_modal_distance, \
                        get_distance_stdev


with open(os.path.join(app.root_path, 'static', 'data', 'classes.json')) as f:
    classes = loads(f.read())

@app.route("/")
def index():
    """Index page."""
    return render_template("index.html", title=gettext("Home"),
                           mean_distance=get_mean_distance(classes),
                           modal_distance=get_modal_distance(classes),
                           distance_stdev=get_distance_stdev(classes))

@app.route("/about")
def about():
    """About page."""
    return render_template("about.html", title=gettext("About"))

@app.route("/lang/<language>")
def lang(language=None):
    """Language pages."""
    session["language"] = language
    return redirect(url_for("index"))

@babel.localeselector
def get_locale():
    """Get current language."""
    try:
        language = session['language']
    except KeyError:
        language = None
    return language if language else request.accept_languages.best_match(LANGUAGES.keys())

@socketio.on('event')
def on_connect(message):
    """Called when the user connects to the websocket."""
    print('Received Message: {0}'.format(str(message)))

@socketio.on('update')
def update_x(message):
    """Called when the slider's value is updated."""
    print("Update: {0}".format(str(message)))
    print("Getting the required data...")
    start, end = message['data'][0], message['data'][1]
    data = get_range(classes, start, end)
    print("Done! Now sending data...")
    socketio.emit('data', data)
