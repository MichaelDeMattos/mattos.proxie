# -*- coding: utf-8 -*-

from proxie import Proxie
from flask import Flask, render_template, jsonify
from views import proxie

# Application
app = Flask(__name__, template_folder="templates")

# Config
app.config.update(
    DEGUB = True,
    SECRET_KEY = None
)

# Blueprints
app.register_blueprint(proxie)

