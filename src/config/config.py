BASE_URL="https://www.cowin.gov.in"
DISTRICT_SEARCH_URL="/api/v2/appointment/sessions/public/calendarByDistrict?district_id={{district_id}}&date={{date}}"

MIN_AGE_LIMIT = 18
SLEEP_TIME_IN_SECONDS = 60

DISTRICT_CODE_TO_CITY_MAPPING = [
	{"district_code": "650", "district_name": "GAUTAM BUDDHA NAGAR", "active": True}
]

CENTER_PREFERENCE_DATA = {
	"GHAZIABAD": [
		{"name": "UPHC Makanpur 18 to 44", "district_name": "GHAZIABAD", "center_id": "697507", "desired_capacity": "1", "vaccine_preference": "any"}
	],
	"BAREILLY": [
		{"name": "Air Force Station 18", "district_name": "BAREILLY", "center_id": "695232", "desired_capacity": "2", "vaccine_preference": "any"}
	]
}

## Communication configs
COMMUNICATION_FORMAT = "PIN {{pin_code}} - {{seats_available}} vaccines available at {{center_name}} in {{district_name}}, {{state}} on {{date}} for {{min_age_limit}}%2B people. Hurry!! Book fast. https://selfregistration.cowin.gov.in"

BEEPS_ENABLED = True
COWSAY_ENABLED = True

# SMS
SMS_COMMUNICATIONS_ENABLED = False
TWILIO_ACCOUNT_SID = "XXXXXXXXXXXXXXXXXXXXXXXXX"
TWILIO_AUTH_TOKEN = "XXXXXXXXXXXXXXXXXXXXXXXXX"
TWILIO_SENDER_PHONE_NUMBER = "1234567"

# Telegram
TELEGRAM_COMMUNICATIONS_ENABLED = False
TELEGRAM_API_ID = "XXXXXXXXXXXXXXXXXXXXXXXXX"
TELEGRAM_API_HASH = "XXXXXXXXXXXXXXXXXXXXXXXXX"
TELEGRAM_BOT_TOKEN = "XXXXXXXXXXXXXXXXXXXXXXXXX"
TELEGRAM_SENDER_PHONE_NUMBER = "9876543210"
TELEGRAM_BOT_SEND_MESSAGE_ENDPOINT = "https://api.telegram.org/bot{{telegram_bot_token}}/sendMessage?chat_id={{receiver_id}}&parse_mode=Markdown&text={{message}}"

TELEGRAM_ALL_SUBSCRIBERS = [
							"-534898187"  # Group Covid Vaccine Updates (18+)
						]

USER_TO_DISTRICT_CODE_PREFERENCE_MAPPING = {
	"17648279947986": ["GAUTAM BUDDHA NAGAR", "GHAZIABAD"]
}
