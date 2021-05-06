from config import MIN_AGE_LIMIT
from notification import beep_notification
from notification import meow

res = []

def filter(data, min_vacancy_required):
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
            if session.get('min_age_limit', 1000) <= MIN_AGE_LIMIT and session.get('available_capacity', 0) >= min_vacancy_required:
                beep_notification()

                message = "\n!!! ----- IT'S A MATCH ----- !!!\n" + "Book " + center_details["name"] + " on the " + session["date"]
                meow(message)
                
                # print(session, center_details)
                res.append({**center_details, **session})

    return res