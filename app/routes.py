"""Routing functions for Flask."""
from app import app
from flask import render_template

@app.route("/")
def index():
    """Index page."""
    return render_template("index.html", title="Home")
