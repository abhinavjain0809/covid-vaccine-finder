from collections import namedtuple
from config.config import CENTER_PREFERENCE_DATA
from config.config import MIN_AGE_LIMIT

def validate_center_preferences(center_details, session):
	if (len(CENTER_PREFERENCE_DATA) == 0):
		return default_center_validations(session);

	custom_center_preferences = load_custom_center_preferences(center_details["center_id"])
	if (custom_center_preferences == None):
		return False
	
	return custom_center_validations(session, custom_center_preferences)

def load_custom_center_preferences(center_id):
	for data in CENTER_PREFERENCE_DATA:
		custom_center_preferences = namedtuple("CenterPreferences", data.keys())(*data.values())
		if (custom_center_preferences.center_id == str(center_id)):
			return custom_center_preferences

	return None

def default_center_validations(session):
	if is_age_valid(session) and is_center_having_enough_capacity(session, 1):
		return True

	return False

def custom_center_validations(session, custom_center_preferences):
	if is_age_valid(session) and is_center_having_enough_capacity(session, custom_center_preferences.desired_capacity) and is_perferred_vaccine_available(session, custom_center_preferences.vaccine_preference):
		return True

	return False

def is_age_valid(session):
	if session.get('min_age_limit', 1000) <= MIN_AGE_LIMIT:
		return True

	return False

def is_center_having_enough_capacity(session, desired_capacity):
	return session.get('available_capacity', 0) >= int(desired_capacity)

def is_perferred_vaccine_available(session, vaccine_preference):
	if (vaccine_preference == "any"):
		return True

	return session["vaccine"] == vaccine_preference