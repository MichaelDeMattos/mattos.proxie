# -*- coding: utf-8 -*-

from flask import Flask, Blueprint, render_template

home = Blueprint('home', __name__, template_folder="templates", 
                 static_url_path="/home/static", static_folder="static")

class Project(object):
    def __init__(self, *args):
        ...
    
    @home.route("/", methods=["GET"])
    def index():
        return render_template("home.html")