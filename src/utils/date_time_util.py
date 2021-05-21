from datetime import datetime, timedelta

def get_date_array():
    all_dates = []
    
    # Get current date
    today = datetime.today()
    all_dates.append(today.strftime("%d-%m-%Y"))

    # Get today + 7 days
    today_plus_7_days = datetime.today() + timedelta(days=7)
    all_dates.append(today_plus_7_days.strftime("%d-%m-%Y"))

    # Get today + 14 days
    today_plus_14_days = datetime.today() + timedelta(days=14)
    all_dates.append(today_plus_14_days.strftime("%d-%m-%Y"))

    # Get today + 21 days
    today_plus_21_days = datetime.today() + timedelta(days=21)
    all_dates.append(today_plus_21_days.strftime("%d-%m-%Y"))

    return all_dates