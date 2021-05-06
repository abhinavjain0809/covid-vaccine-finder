BASE_URL="https://www.cowin.gov.in"
DISTRICT_SEARCH_URL="/api/v2/appointment/sessions/public/calendarByDistrict?district_id={{district_id}}&date={{date}}"

MIN_AGE_LIMIT = 18
SLEEP_TIME_IN_SECONDS = 60

DISTRICT_CODE_TO_CITY_MAPPING = [
	{"district_code": "637", "district_name": "BAREILLY", "active": True},
	{"district_code": "680", "district_name": "PILIBHIT", "active": True},
	{"district_code": "650", "district_name": "NOIDA", "active": False},
	{"district_code": "651", "district_name": "GHAZIABAD", "active": False}
]

CENTER_PREFERENCE_DATA = [
	{"name": "Civil Line 18 to 44", "district_name": "BAREILLY", "center_id": "692558", "desired_capacity": "2", "vaccine_preference": "any"},
	{"name": "Air Force Station 18", "district_name": "BAREILLY", "center_id": "695232", "desired_capacity": "2", "vaccine_preference": "any"},
	{"name": "Nawabganj CHC 18 to 44", "district_name": "BAREILLY", "center_id": "693640", "desired_capacity": "2", "vaccine_preference": "any"},
	{"name": "IzzatNagar UPHC 18 to 44", "district_name": "BAREILLY", "center_id": "692570", "desired_capacity": "2", "vaccine_preference": "any"}
]
