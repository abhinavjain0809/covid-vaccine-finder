from datetime import datetime, timedelta

def get_date_array():
    all_dates = []
    
    # Get current date
    today = datetime.today()
    all_dates.append(today.strftime("%d-%m-%Y"))

    # Get today + 3 days
    today_plus_3_days = datetime.today() + timedelta(days=3)
    all_dates.append(today_plus_3_days.strftime("%d-%m-%Y"))

    # Get today + 7 days
    today_plus_7_days = datetime.today() + timedelta(days=7)
    all_dates.append(today_plus_7_days.strftime("%d-%m-%Y"))

    # Get today + 11 days
    today_plus_11_days = datetime.today() + timedelta(days=11)
    all_dates.append(today_plus_11_days.strftime("%d-%m-%Y"))

    return all_dates