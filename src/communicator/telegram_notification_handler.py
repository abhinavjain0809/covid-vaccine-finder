import telebot
from telethon.sync import TelegramClient
from telethon.tl.types import InputPeerUser, InputPeerChannel
from telethon.tl.functions.contacts import ResolveUsernameRequest
from telethon import TelegramClient, sync, events, functions, types
from config.config import TELEGRAM_API_ID
from config.config import TELEGRAM_API_HASH
from config.config import TELEGRAM_BOT_TOKEN
from config.config import TELEGRAM_SENDER_PHONE_NUMBER
from config.config import TELEGRAM_BOT_SEND_MESSAGE_ENDPOINT
# from config.config import TELEGRAM_ALL_SUBSCRIBERS
import requests

# client = None
# username_user_id_mapping = {}

# def send_telegram_message_as_abhinav_jain(message):
# 	client = TelegramClient('session', TELEGRAM_API_ID, TELEGRAM_API_HASH)
	   
# 	client.connect()
	  
# 	if not client.is_user_authorized():
	   
# 	    client.send_code_request(TELEGRAM_SENDER_PHONE_NUMBER)
	      
# 	    client.sign_in(TELEGRAM_SENDER_PHONE_NUMBER, input('Enter the code: '))
	   

# 	try:
# 	    receiver = InputPeerUser(1764827994, -663196234156636134)

# 	    client.send_message(receiver, message, parse_mode='html')
# 	except Exception as e:
	      
# 	    # there may be many error coming in while like peer
# 	    # error, wwrong access_hash, flood_error, etc
# 	    print("Error while sending Telegram communication: ", e);
	  
# 	# disconnecting the telegram session 
# 	client.disconnect()

def send_telegram_message(message, username):
	# global client
	# client = init_client()

	# for username in TELEGRAM_ALL_SUBSCRIBERS:
	# receiver_id = get_receiver_id(client, username)
	receiver_id = username

	try:
		url = TELEGRAM_BOT_SEND_MESSAGE_ENDPOINT.replace("{{telegram_bot_token}}", TELEGRAM_BOT_TOKEN).replace("{{receiver_id}}", str(receiver_id)).replace("{{message}}", message)
		requests.get(url)
	except Exception as e:
		print("Error calling telegram bot API to send message to user ", username)

# def init_client():
# 	global client
# 	if (client is None):
# 		print("init telegram client")
# 		client = TelegramClient('session', TELEGRAM_API_ID, TELEGRAM_API_HASH)
# 		client.connect()

# 		try:
# 			if not client.is_user_authorized():
# 			    client.send_code_request(TELEGRAM_SENDER_PHONE_NUMBER)
# 			    client.sign_in(TELEGRAM_SENDER_PHONE_NUMBER, input('Enter the code: '))
# 		except Exception as e:
# 			print("Error while initializing telegram client: ", e);

# 	return client

# def get_receiver_id(client, username):
# 	global username_user_id_mapping
# 	if (username in username_user_id_mapping):
# 		return username_user_id_mapping[username]
# 	try:
# 		result = client(functions.contacts.ResolveUsernameRequest(username=username))
# 		receiver_id = result.users[0].id
# 		username_user_id_mapping[username] = receiver_id

# 		return receiver_id
# 	except Exception as e:
# 		print("Error when fetching receiver id from username ", username)
