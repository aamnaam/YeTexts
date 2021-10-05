import os
from dotenv import load_dotenv
import requests
from flask import Flask, request, Response
from twilio.twiml.messaging_response import MessagingResponse
from pymongo import MongoClient

app = Flask(__name__)

kanye_endpoint = "https://api.kanye.rest"
random_inspire_endpoint = "https://zenquotes.io/api/random"

# MongoDB setup
load_dotenv()
cluster = MongoClient(os.environ.get("DB-CONNECTION"))
db = cluster["ye_texts"]
to_verify_collection = db["requesting_verification"]
verified_users_collection = db["verified_users"]

# to assign ID's to registering users for when they are verified
num_users = verified_users_collection.count_documents({})


@app.route('/', methods=['GET'])
def index() -> str:
    return "<h1>YeTexts<h1>"


@app.route('/api/register', methods=['POST'])
def register() -> Response:
    """Receives registration data and adds to 'to_verify_collection'"""

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

    res = Response(status=200)
    return res


@app.route('/api/ye', methods=['POST'])
def send_quote() -> str:
    """Returns preset response to a WhatsApp message"""

    msg = request.form.get('Body')
    res = MessagingResponse()
    if msg == 'ye':
        res.message(get_ye_quote()) 
    elif msg == 'inspire':
        res.message(get_inspirational_quote())
    else:
        res.message(f"Command not found: '{msg}'")
    return str(res)


def get_ye_quote() -> str:
    res = requests.get(kanye_endpoint)
    return res.json()['quote']


def get_inspirational_quote() -> str:
    res = requests.get(random_inspire_endpoint)
    return res.json()['q']


def generate_user_id() -> int:
    global num_users
    num_users += 1
    return num_users


def main() -> None:
    app.run()


if __name__ == '__main__':
    main()
