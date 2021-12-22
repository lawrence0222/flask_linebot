from flask import render_template, request, session
import requests
import json
from flask import Blueprint
from models import *

identify = Blueprint("identify", __name__,template_folder="templates")


@identify.route("/")
def index():
    return render_template("line_login.html")


@identify.route("/1", methods=["POST", "GET"])
def login():
    code = request.args.get("code")
    data = {
        "grant_type": "authorization_code",
        "code": code,
        "redirect_uri": "https://linebotlawrence.herokuapp.com/1",
        "client_id": 1656730482,
        "client_secret": "d4e1b8138b743cd8de627d592b967f07",
    }
    response_1 = requests.post("https://api.line.me/oauth2/v2.1/token", data=data)
    json_1 = json.loads(response_1.text)
    data2 = {"id_token": json_1["id_token"], "client_id": 1656730482}
    response_2 = requests.post("https://api.line.me/oauth2/v2.1/verify", data=data2)
    print(response_2.text)
    json_2 = json.loads(response_2.text)
    user_id = json_2["sub"]
    name = json_2["name"]
    user_pic = json_2["picture"]

    insert(user_id, name, user_pic)
    if check(user_id) == 1:
        return render_template('manager.html',user_info= user_info())
    return render_template('usr.html',segment_details=msg(user_id))