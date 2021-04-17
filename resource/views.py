# -*- coding: utf-8 -*-

from flask import Flask, Blueprint, jsonify, make_response
from resource.controller import ControllerFormatProxie

resource = Blueprint("resource", __name__)

class Project(object):
    def __init__(self, *args):
        ...

    """ This is route main for public API """
    @resource.route("/<string:id_country>", methods=["GET"])
    def index(id_country=None):
        proxies = ControllerFormatProxie().proxie_layout(id_country.lower())
        return make_response(jsonify(proxies), 201)