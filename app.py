# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    app.py                                             :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: michael.ortiz <michael.ortiz@dotpyc.com    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/06/18 23:55:50 by michael.ort       #+#    #+#              #
#    Updated: 2022/06/18 23:58:40 by michael.ort      ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from flask_restful import Api
from resource.controller import ProxieAPI
from flask import Flask, make_response, render_template

# Application
app = Flask(__name__)

# Config
app.config.update(
    DEGUB=True,
    SECRET_KEY=None,
)

# Routes
@app.route("/", methods=["GET"])
def index():
    return make_response(
        render_template("index.html"),
        200
    )


# API
api = Api(app)
api.add_resource(ProxieAPI, "/", "/api/list_proxie", endpoint="list")
