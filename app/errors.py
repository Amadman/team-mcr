"""Error handler functions for web page errors -- i.e. 404."""

from flask import render_template, flash
from app import app

@app.errorhandler(401)
@app.errorhandler(404)
def page_not_found(err):
    """Returns a rendered error page that displays details about the error."""
    flash("{}: {}".format(err.code, err.description))
    return render_template("index.html"), err.code
