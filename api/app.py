import os
from dotenv import load_dotenv
import requests

from flask import Flask, request, render_template
from twilio.twiml.messaging_response import MessagingResponse
from pymongo import MongoClient


app = Flask(__name__)
kanye_api: str = 'https://api.kanye.rest'
cluster = MongoClient(os.environ.get("DB-CONNECTION"))

db = cluster["ye_texts"]
to_verify_collection = db["requesting_verification"]


@app.route('/')
def home() -> str:
    return 'YeTexts'


@app.route('/', methods=['GET'])
def index() -> str:
    return render_template('index.html')


@app.route('/api/register', methods=['POST'])
def register() -> None:
    if request.method == 'POST':
        user_details = request.json
        name = user_details['name']
        WAid = user_details['WAid']

    print(name + ' ' + WAid)
    new_user_data = {
        "_id": generate_user_id(),
        "name": name,
        "WAid": WAid
    }

    to_verify_collection.insert_one(new_user_data)


@app.route('/api/ye', methods=['POST'])
def send_quote() -> str:
    """Returns preset response to a WhatsApp message"""

    msg = request.form.get('Body')
    res = MessagingResponse()
    if msg == 'ye':
        res.message(get_ye_quote()) 
    else:
        res.message(f"Command not found: '{msg}'")
    return str(res)


def get_ye_quote() -> str:
    res = requests.get(kanye_api)
    return res.json()['quote']


def generate_user_id() -> int:
    pass


def main() -> None:
    app.run()


if __name__ == '__main__':
    main()
