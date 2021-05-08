BASE_URL="https://www.cowin.gov.in"
DISTRICT_SEARCH_URL="/api/v2/appointment/sessions/public/calendarByDistrict?district_id={{district_id}}&date={{date}}"

MIN_AGE_LIMIT = 18
SLEEP_TIME_IN_SECONDS = 60

DISTRICT_CODE_TO_CITY_MAPPING = [
	{"district_code": "637", "district_name": "BAREILLY", "active": True},
	{"district_code": "680", "district_name": "PILIBHIT", "active": True},
	{"district_code": "650", "district_name": "GAUTAM BUDDHA NAGAR", "active": True},
	{"district_code": "651", "district_name": "GHAZIABAD", "active": True},
	{"district_code": "622", "district_name": "AGRA", "active": True},
	{"district_code": "265", "district_name": "BANGALORE URBAN", "active": True},
	{"district_code": "654", "district_name": "GORAKHPUR", "active": True},
	{"district_code": "539", "district_name": "COIMBATORE", "active": True},
	{"district_code": "154", "district_name": "AHMEDABAD", "active": True},
	{"district_code": "670", "district_name": "LUCKNOW", "active": True},
	{"district_code": "505", "district_name": "JAIPUR I", "active": True},
	{"district_code": "506", "district_name": "JAIPUR II", "active": True}
]

CENTER_PREFERENCE_DATA = {
	"BAREILLY": [
		{"name": "Civil Line 18 to 44", "district_name": "BAREILLY", "center_id": "692558", "desired_capacity": "2", "vaccine_preference": "any"},
		{"name": "Air Force Station 18", "district_name": "BAREILLY", "center_id": "695232", "desired_capacity": "2", "vaccine_preference": "any"},
		{"name": "Nawabganj CHC 18 to 44", "district_name": "BAREILLY", "center_id": "693640", "desired_capacity": "1", "vaccine_preference": "any"},
		{"name": "IzzatNagar UPHC 18 to 44", "district_name": "BAREILLY", "center_id": "692570", "desired_capacity": "2", "vaccine_preference": "any"}
	]
}

## Communication configs
COMMUNICATION_FORMAT = "{{seats_available}} vaccines available at {{center_name}} in {{district_name}}, {{state}} on {{date}} for {{min_age_limit}}%2B people. Hurry!! Book fast."

BEEPS_ENABLED = True
COWSAY_ENABLED = True

# SMS
SMS_COMMUNICATIONS_ENABLED = False
TWILIO_ACCOUNT_SID = "ACdd95545b95455c8af8e8c117e9ab3040"
TWILIO_AUTH_TOKEN = "c7854d36e9d295a4066a327c2fe62c97"
TWILIO_SENDER_PHONE_NUMBER = "+18053015945"

# Telegram
TELEGRAM_COMMUNICATIONS_ENABLED = True
TELEGRAM_API_ID = "4308896"
TELEGRAM_API_HASH = "a6378f9394038196405acb44abddf9c6"
TELEGRAM_BOT_TOKEN = "1709139154:AAEypOxBigq7PuuRh_oxue35qTu-cuczNWs"
TELEGRAM_SENDER_PHONE_NUMBER = "+919547177346"
TELEGRAM_BOT_SEND_MESSAGE_ENDPOINT = "https://api.telegram.org/bot{{telegram_bot_token}}/sendMessage?chat_id={{receiver_id}}&parse_mode=Markdown&text={{message}}"

TELEGRAM_ALL_SUBSCRIBERS = [
							"1764827994", # Abhinav Jain (Me)
							"1818399238", # Kavisha Agarwal
							"1731027243", # Atishay Jain
							"1027094505", # Shreyas Tayade
							"628839243",  # Naman Jain
							"1488648782", # Himanshu Jain
							"1696418807", # Mohit Garg
							"847799044",  # Shripad Nadiger
							"1745184479", # Sahil Jain
							"1757566184", # Antarin Karmakar
							"1077889025", # Prince Choudhary
							"1062100223", # Aayush Jain
							"989757584",  # R...M...
							"1065516880", # Dharmesh Ruprela
							"1523795852", # Ayush Pant
							"1784150570", # Rani Selvaraj
							"523321897",  # Darshak Patel
							"1153269713", # Abhinav Chandra
							"1004970145", # El Professor,
							"646646654",  # Aspired For Studies
							"1760078804", # Shubh
							"1427952920", # Ekta Arora
							"1048670877", # Soumya
							"1185161213", # Somavroto Rakshit
							"1443350314", # Tanuja Sahu
							"927268478",  # Nishant Singh
							"694528317",  # Rishabh Saxena
							"1280540101", # Aman Deep
							"-534898187"  # Group Covid Vaccine Updates (18+)
						]

USER_TO_DISTRICT_CODE_PREFERENCE_MAPPING = {
	"1764827994": ["GAUTAM BUDDHA NAGAR", "GHAZIABAD"],
	"1818399238": ["BAREILLY", "PILIBHIT"],
	"1731027243": ["GAUTAM BUDDHA NAGAR", "GHAZIABAD"],
	"628839243": ["AGRA"],
	"1488648782": ["AGRA"],
	"1745184479": ["AGRA"],
	"1696418807": ["BANGALORE URBAN"],
	"1757566184": ["GAUTAM BUDDHA NAGAR", "GHAZIABAD"],
	"1077889025": ["GAUTAM BUDDHA NAGAR"],
	"1065516880": ["GORAKHPUR"],
	"1523795852": ["BAREILLY", "PILIBHIT"],
	"1784150570": ["COIMBATORE"],
	"523321897": ["AHMEDABAD"],
	"1153269713": ["GAUTAM BUDDHA NAGAR", "GHAZIABAD"],
	"1004970145": ["BAREILLY", "PILIBHIT"],
	"646646654": ["LUCKNOW"],
	"1760078804": ["LUCKNOW"],
	"1427952920": ["BANGALORE URBAN"],
	"1048670877": ["BANGALORE URBAN"],
	"1185161213": ["BANGALORE URBAN"],
	"1443350314": ["JAIPUR I", "JAIPUR II"],
	"927268478": ["JAIPUR I", "JAIPUR II"],
	"694528317": ["BAREILLY", "PILIBHIT"],
	"1280540101": ["GORAKHPUR"]
}
