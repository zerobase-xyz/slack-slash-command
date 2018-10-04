import os
import random
import requests
from flask import Flask, jsonify

app = Flask(__name__)

# CUSTOM SEARCH API周りの設定
SEARCH_API_KEY = os.environ.get("SEARCH_API_KEY")
ENGINE_ID = os.environ.get("ENGINE_ID")
URL_TEMPLATE = "https://www.googleapis.com/customsearch/v1"

def get_image_url(search_word):
    """
    GOOGLE CUSTOM SEARCH APIからキーワードで画像のURLを取得する
    """

    params = {
        'key': SEARCH_API_KEY,
        'cx': ENGINE_ID,
        'searchType': 'image',

    response = requests.get(URL_TEMPLATE, params=params)
    data = response.json()

    if "items" not in data:
        raise Exception('no images were found.')

    random_item = random.choice(data['items'])

    return random_item['link']

def build_message(url):
    """
    Slack用のメッセージを作成
    """
    post_message = {}
    post_message["text"] = ""
    post_message["attachments"] = [{ "image_url": url}]
    return post_message


@app.route('/cat', methods=['POST'])
def slack_cat():
    try:
        # urlを複数取得する
        url = get_image_url('cat')
    except Exception as e:
        # urlが取得できなかった場合は投稿しない
        return jsonify({'text': e})

    # slack用のメッセージを作成
    post_msg = build_message(url)

    return jsonify(post_msg)

@app.route('/')
def hello():
    word = "Hello World"
    return word

if __name__ == "__main__":
    app.run()
