from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from twilio.rest import Client

# Twilio credentials
account_sid = 'your_account_sid_here'
auth_token = 'your_auth_token_here'

app = Flask(__name__)

@app.route('/sms', methods=['POST'])
def sms_reply():
    """Respond to incoming calls with a simple text message."""
    resp = MessagingResponse()
    resp.message("Hello, thanks for texting me!")
    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)
