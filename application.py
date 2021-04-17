# -*- coding: utf-8 -*-

from flask import Flask, jsonify
from resource.views import resource
from home.views import home

# Application
app = Flask(__name__)

# Config
app.config.update(
    DEGUB = True,
    SECRET_KEY = None,
)

# Blueprints
app.register_blueprint(resource)
app.register_blueprint(home)
