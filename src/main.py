import time
from config.config import SLEEP_TIME_IN_SECONDS
from config.config import DISTRICT_CODE_TO_CITY_MAPPING
from fetch_cowin_data import fetch_data
from filter_data import filter
from utils.date_time_util import get_date_array

def process(district_code, date):
    data = fetch_data(district_code, date)
    matched_sessions = filter(data)

def main():
    print("\n\nLet me find you a vaccine, while you sit back and relax :)\n\n")
    while True:
        for mapping in DISTRICT_CODE_TO_CITY_MAPPING:
            if (mapping.get("active") == False):
                continue
            
            for date in get_date_array():
                print(mapping.get('district_name'), end = " - ")
                print(date, end = " - ")
                
                process(mapping.get('district_code'), date)

            print()
            
        print("Sleeping for {} seconds".format(SLEEP_TIME_IN_SECONDS) + "\n")
        time.sleep(SLEEP_TIME_IN_SECONDS)


if __name__=="__main__":
    main()
