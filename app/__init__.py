from urllib.error import HTTPError
import logging
import os

from flask import Flask
from config import Config

logging.basicConfig(level=os.environ.get("LOGLEVEL", "INFO"))
log = logging.getLogger(__name__)

__version__ = "0.0.1"

app = Flask(__name__)
app.config.from_object(Config)

# Stop the jinja2 templating from putting in unnecessary whitespace.
app.jinja_env.trim_blocks = True
app.jinja_env.lstrip_blocks = True

def setup_webapp():
    """General setup tasks that are run upon application launch."""
    log.info("Starting webapp...")
    log.info("No startup tasks required at this early stage.")

setup_webapp()

from app import routes, errors
