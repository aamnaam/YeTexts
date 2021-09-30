from flask import Flask, request, render_template
from twilio.twiml.messaging_response import MessagingResponse
from applying_users.models import ApplyingUser
import requests

app = Flask(__name__)

kanye_api: str = 'https://api.kanye.rest'

@app.route('/')
def home() -> str:
    return 'YeTexts'


@app.route('/api/register', methods=['GET', 'POST'])
def index() -> str:
    if request.method == 'POST':
        user_details = request.form
        name = user_details['name']
        WAid = user_details['WAid']
    return render_template('index.html')


@app.route('/api/ye', methods=['POST'])
def send_quote() -> str:
    '''Returns preset response to a WhatsApp message'''

    msg = request.form.get('Body')
    sender_id = request.form.get('WaId')
    res = MessagingResponse()
    if msg == 'ye':
        res.message(get_ye_quote()) 
    else:
        res.message(f"Command not found: '{msg}'")
    return str(res)


def get_ye_quote() -> str:
    res = requests.get(kanye_api)
    return res.json()['quote']


def main() -> None:
    app.run()


if __name__ == '__main__':
    main()
    