import sys
import json
from config.config import SMS_COMMUNICATIONS_ENABLED
from config.config import TELEGRAM_COMMUNICATIONS_ENABLED
from config.config import BEEPS_ENABLED
from config.config import COWSAY_ENABLED
from twilio.rest import Client
from communicator.telegram_notification_handler import send_telegram_message

def bell_notification():
    sys.stdout.write('\a')
    sys.stdout.flush()

def beep_notification():
    if (not BEEPS_ENABLED):
        return

    from beepy import beep

    beep(sound=1)

def meow(message):
    if (not COWSAY_ENABLED):
        return

    import cowsay

    cowsay.meow(message)

def text_notification(message_to_send):
    if (not SMS_COMMUNICATIONS_ENABLED):
        return
    
    account_sid = "ACdd95545b95455c8af8e8c117e9ab3040"
    auth_token = "c7854d36e9d295a4066a327c2fe62c97"

    client = Client(account_sid, auth_token)

    message = client.messages.create(body = message_to_send, from_ = "+18053015945", to = "+919547177346")
    message = client.messages.create(body = message_to_send, from_ = "+18053015945", to = "+918972984598")

def telegram_message(message_to_send, username):
    if (not TELEGRAM_COMMUNICATIONS_ENABLED):
        return
    
    send_telegram_message(message_to_send, username)