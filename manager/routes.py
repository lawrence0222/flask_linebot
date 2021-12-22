from flask import render_template, request, redirect, url_for
import requests
import json
from flask import Blueprint
from models import *
manager = Blueprint("manager", __name__,template_folder="templates", url_prefix='/manager')


@manager.route("/", methods=["POST", "GET"])
def index():
    return render_template("manager.html",user_info= user_info())



@manager.route("/Grouping", methods=["POST", "GET"])
def submit():
    request_list = list(request.form.keys())
    for j in request_list:
        if j=='nm':
            user_id = request.form[j]
        else:
            insert_label(user_id,j)
    return render_template("manager.html",user_info= user_info())



@manager.route("/GroupMail", methods=["POST", "GET"])
def submit2():
    request_list = list(request.form.keys())
    print(request_list)
    group = []
    for i in request_list:
        if i != "text":
            group.append(i)
    group_msg(group,request.form["text"])
    return render_template("manager.html",user_info= user_info())



@manager.route("/PrivateMessage", methods=["POST", "GET"])
def submit3():
    user_id = request.form['nm']
    text = request.form['text']
    update_msg(user_id,text)
    return render_template("manager.html",user_info= user_info())