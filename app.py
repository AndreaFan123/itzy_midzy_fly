from flask import Flask, request, abort

from linebot.v3 import (
    
    WebhookHandler
)
# from linebot.v3.exceptions import (
#     InvalidSignatureError
# )
from linebot.v3.messaging import (
    Configuration,
    # ApiClient,
    # MessagingApi,
    # ReplyMessageRequest,
    # TextMessage
)
from linebot.v3.webhooks import (
    MessageEvent, TextMessage, TextSendMessage, StickerSendMessage, ImageSendMessage
)

from dotenv import load_dotenv

import os
import json

load_dotenv()

app = Flask(__name__)

access_token = os.getenv('CHANNEL_ACCESS_TOKEN')
channel_secret = os.getenv('CHANNEL_SECRET')
line_bot_api = os.getenv('CHANNEL_ACCESS_TOKEN')
configuration = Configuration(access_token)
handler = WebhookHandler(channel_secret)


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        json_data = json.loads(body)       
        handler.handle(body, signature)
        tk = json_data['events'][0]['replyToken']
        msg = json_data['event'][0]['message']['text']

        if msg == 'yeji':
            img_url = "https://res.cloudinary.com/dbrf4i0rb/image/upload/v1717030120/Screenshot_2024-05-30_at_08.33.37_gwloim.png"
            img_message = ImageSendMessage(original_content_url=img_url, preview_image_url=img_url)
            line_bot_api.reply_message(tk,img_message)
        else:
            text_message = TextSendMessage(text="找不到相關圖片")
            line_bot_api.reply_message(tk, text_message)
    except:
        print(body)

    return 'OK'


if __name__ == "__main__":
    app.run()
# from flask import Flask, request
# from dotenv import load_dotenv
# from linebot.v3 import LineBotApi, WebhookHandler
# from linebot.v3.webhooks import TextSendMessage, ImageSendMessage
# import os
# import json

# load_dotenv()

# app = Flask(__name__)

# @app.route('/callback', methods=['POST'])
# def callback():
#     body = request.get_data(as_text=True)
#     try:
#         json_data = json.loads(body)
#         access_token = os.getenv('CHANNEL_ACCESS_TOKEN')
#         secret = os.getenv('LINE_SECRET')
#         line_bot_api = LineBotApi(access_token)
#         handler = WebhookHandler(secret)
#         signature = request.headers['X-Line-Signature']
#         handler.handle(body, signature)
#         tk = json_data['events'][0]['replyToken']
#         msg = json_data['events'][0]['message']['text']

#         if msg == 'yeji':
#             img_url="https://asset.cloudinary.com/dbrf4i0rb/cfed8d5e3267b1b763c557db3d68d724"
#             image_message = ImageSendMessage(original_content_url=img_url, preview_image_url=img_url)
#             line_bot_api.reply_message(tk, image_message)
#         else:
#             text_message = TextSendMessage(text="找不到相關圖片")
#             line_bot_api.reply_message(tk, text_message)
#     except:
#         print(body)
#     return 'OK'

# if __name__ == '__main__':
#     app.run()

