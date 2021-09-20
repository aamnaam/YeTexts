from flask import Flask, request, render_template
from twilio.twiml.messaging_response import MessagingResponse
from applying_users.models import ApplyingUser

app = Flask(__name__)


@app.route('/api/register', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        user_details = request.form
        name = user_details['name']
        WAid = user_details['WAid']
    return render_template('index.html')


@app.route('/api/ye', methods=['POST'])
def send_quote():
    msg = request.form.get('Body')
    sender_id = request.form.get('WaId')
    # print(str(request.form))
    res = MessagingResponse()
    res.message(f"You said: {str(request.form)}")
    return str(res)


if __name__ == '__main__':
    app.run()
