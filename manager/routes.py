from re import S
import re
from flask import render_template, request, redirect, url_for
import requests
import json
from flask import Blueprint
from models import *
from linebot.models import TextSendMessage
from linebot.exceptions import LineBotApiError
from linebot import LineBotApi




manager = Blueprint("manager", __name__,template_folder="templates", url_prefix='/manager')

line_bot_api = LineBotApi('lZjUhkDwED79lPFD/0k68acKfkoxtxkS4rdsmK3epf4XuiYaqojTL72gqFxACeO4QtettJ0X+/GuTMJMxm/q7B/Cq1+qbZzp3H7oXQTCyfCmFvpACekbwJ8VeaTQE5kihkBDRLivsM0hSEcWcGGFDwdB04t89/1O/w1cDnyilFU=')


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
    user_list = id_in_group(group)
    for i in user_list:
        line_bot_api.push_message(i[0], TextSendMessage(text=request.form["text"]))
    group_msg(group,request.form["text"])
    return render_template("manager.html",user_info= user_info())

@manager.route("/GroupMail/iden", methods=["POST", "GET"])
def iden():
    request_list = list(request.form.keys())
    group = []
    for i in request_list:
        if i != "text":
            group.append(i)
    user_all = user_info()
    id_list = id_in_group(group)
    for id in user_all[0]:
        if id in id_list:
            user_all.remove(id)

    return render_template("manager.html",user_info= user_all)



@manager.route("/PrivateMessage", methods=["POST", "GET"])
def submit3():
    user_id = request.form['nm']
    user_text = request.form['text']
    update_msg(user_id,user_text)
    line_bot_api.push_message(user_id, TextSendMessage(text=user_text))
    return render_template("manager.html",user_info= user_info())