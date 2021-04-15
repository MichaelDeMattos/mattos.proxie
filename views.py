# -*- coding: utf-8 -*-

from flask import Flask, Blueprint, jsonify, make_response
from controller import ControllerFormatProxie

proxie = Blueprint("mattos.proxie", __name__)

class Project(object):
    def __init__(self, *args):
        ...

    """ This is route main for public API """
    @proxie.route("/<string:id_country>", methods=["GET"])
    def index(id_country=None):
        proxies = ControllerFormatProxie().proxie_layout(id_country.lower())
        return make_response(jsonify(proxies), 201)