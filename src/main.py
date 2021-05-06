# import os
import time
from config import SLEEP_TIME
from fetch_cowin_data import fetch_data
from filter_data import filter
from district_codes import get_all_district_codes
# from data_to_csv import write_data
from date_time_util import get_date_array

def process(district_code, date, min_vacancy_required):
    data = fetch_data(district_code, date)
    matched_sessions = filter(data, min_vacancy_required)
    if matched_sessions:
        pass
    # else:
    #     print("No Match found")


def main():
    # district_code = os.environ.get('DISTRICT_CODE', '650')
    print("\n\nLet me find you a vaccine, while you sit back and relax :)\n\n")
    while True:
        # print("Starting Process")
        for mapping in get_all_district_codes():
            
            for date in get_date_array():
                print(mapping.get('district_name'), end = " - ")
                print(date, end = " - ")
                
                process(mapping.get('district_code'), date, mapping.get('min_vacancy_required'))

            print()
            
        print("Sleeping for {} seconds".format(SLEEP_TIME) + "\n")
        time.sleep(SLEEP_TIME)


if __name__=="__main__":
    main()