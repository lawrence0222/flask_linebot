from flask import render_template, request, redirect, url_for, session
import requests
import json
from flask import Blueprint
from models import *
usr = Blueprint("usr", __name__,template_folder="templates")
 

@usr.route("/", methods=["POST", "GET"])
def index():
    return render_template("usr.html")









