from utils.center_preferences_utils import validate_center_preferences
from notification import beep_notification
from notification import meow
from notification import text_notification
from notification import telegram_message
from config.config import MIN_AGE_LIMIT
from config.config import COMMUNICATION_FORMAT
from config.config import CENTER_PREFERENCE_DATA
from config.config import TELEGRAM_ALL_SUBSCRIBERS
from config.config import USER_TO_DISTRICT_CODE_PREFERENCE_MAPPING

res = []

def filter(data):
    data = data.get('centers', [])
    print("{} centers".format(len(data)))

    for center_data in data:
        center_details = {
            "center_id": center_data.get('center_id'),
            "name": center_data.get('name'),
            "state_name": center_data.get('state_name'),
            "address": center_data.get('address'),
            "block_name": center_data.get('block_name'),
            "pincode": center_data.get("pincode"),
            "district_name": center_data.get("district_name"),
            "fee_type": center_data.get("fee_type")
        }

        session_data = center_data.get('sessions', [])
        for session in session_data:
            udf_center_preferences = get_center_preference_data_for_district(center_details["district_name"].upper())
            if validate_center_preferences(center_details, session, udf_center_preferences):
                beep_notification()
                
                message = get_communication_to_be_sent(center_details, session)
                print (message)

                meow(message)
                
                text_notification(message)
                
                for username in TELEGRAM_ALL_SUBSCRIBERS:
                    if (is_user_interested_in_district_updates(username, center_details["district_name"])):
                        telegram_message(message, username)

    return res

def get_center_preference_data_for_district(district_name):
    return CENTER_PREFERENCE_DATA.get(district_name)

def get_communication_to_be_sent(center_details, session):
    return COMMUNICATION_FORMAT.replace("{{pin_code}}", str(center_details["pincode"])).replace("{{state}}", center_details["state_name"]).replace("{{district_name}}", center_details["district_name"]).replace("{{date}}", session["date"]).replace("{{seats_available}}", str(session["available_capacity"])).replace("{{center_name}}", center_details["name"]).replace("{{min_age_limit}}", str(MIN_AGE_LIMIT))

def is_user_interested_in_district_updates(username, district_name):
    if (username not in USER_TO_DISTRICT_CODE_PREFERENCE_MAPPING):
        return True

    return district_name.upper() in USER_TO_DISTRICT_CODE_PREFERENCE_MAPPING[username]