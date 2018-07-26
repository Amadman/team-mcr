# -*- coding: utf-8 -*-
import os

basedir = os.path.abspath(os.path.dirname(__file__))

LANGUAGES = {
    "en" : "English",
    "es" : "Español",
}

class Config(object):
    SECRET_KEY = os.environ.get("SECRET_KEY") or "fallback"

    # TODO: remove for production
    DEBUG = True
    TEMPLATES_AUTO_RELOAD = True

    BABEL_DEFAULT_LOCALE = "en"
