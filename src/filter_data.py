from utils.center_preferences_utils import validate_center_preferences
from notification import beep_notification
from notification import meow

res = []

def filter(data):
    data = data.get('centers', [])
    print("{} centers".format(len(data)))

    for center_data in data:
        center_details = {
            "center_id": center_data.get('center_id'),
            "name": center_data.get('name'),
            "address": center_data.get('address'),
            "block_name": center_data.get('block_name'),
            "pincode": center_data.get("pincode"),
            "district_name": center_data.get("district_name"),
            "fee_type": center_data.get("fee_type")
        }

        session_data = center_data.get('sessions', [])
        for session in session_data:
            if validate_center_preferences(center_details, session):
                beep_notification()
                message = "\n!!! ----- IT'S A MATCH ----- !!!\n" + "Book " + center_details["name"] + " on the " + session["date"]
                meow(message)

    return res
