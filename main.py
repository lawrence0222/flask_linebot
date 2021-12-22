from flask import Flask, render_template, request, abort
from identify.routes import identify
from usr.routes import usr
from manager.routes import manager


app = Flask(__name__)

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)


@app.route('/')
def index():
    return render_template("line_login.html")



line_bot_api = LineBotApi('lZjUhkDwED79lPFD/0k68acKfkoxtxkS4rdsmK3epf4XuiYaqojTL72gqFxACeO4QtettJ0X+/GuTMJMxm/q7B/Cq1+qbZzp3H7oXQTCyfCmFvpACekbwJ8VeaTQE5kihkBDRLivsM0hSEcWcGGFDwdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('03a9b19024c0ca8f46e731b90f486e18')



@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text))



app.register_blueprint(identify)
app.register_blueprint(usr)
app.register_blueprint(manager)