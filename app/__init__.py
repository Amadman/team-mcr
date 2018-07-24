from urllib.error import HTTPError
import logging
import os

from flask import Flask
from flask_socketio import SocketIO
from config import Config
import json

logging.basicConfig(level=os.environ.get("LOGLEVEL", "INFO"))
log = logging.getLogger(__name__)

__version__ = "0.0.1"

app = Flask(__name__)
app.config.from_object(Config)
socketio = SocketIO(app)

# Stop the jinja2 templating from putting in unnecessary whitespace.
app.jinja_env.trim_blocks = True
app.jinja_env.lstrip_blocks = True

def setup_webapp():
    """General setup tasks that are run upon application launch."""
    log.info("Starting webapp...")
    log.info("No startup tasks required at this early stage.")

@socketio.on('event')
def on_connect(message):
  print('received message: {0}'.format(str(message)))

@socketio.on('update')
def update_x(message):
  print('update: {0}'.format(str(message)))
  with open(os.path.join(app.root_path, 'static', 'data', 'new_schools.json')) as f:
    data = json.load(f)
  socketio.emit('data', data)

setup_webapp()

from app import routes, errors

if __name__ == '__main__':
  socketio.run(app)
