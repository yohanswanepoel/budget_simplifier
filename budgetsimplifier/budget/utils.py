from datetime import date
from datetime import timedelta

def fortnightly_cycles_current_month(start_date):
    #return pay_cycles_in_a_month(start_date, date.today(), 14)
    print (date(2019, 8, 1))
    return pay_cycles_in_a_month(start_date, date(2019, 8, 1), 14)

def pay_cycles_in_a_month(start_date, check_date, frequency):
    frequency = 14
    previous_pay = get_previous_pay_date(start_date, check_date, frequency)
    # Check if month is in this month
    pays_in_month = 0
    if previous_pay.month == check_date.month:
         # First check back
        pays_in_month = 1
        tempDate = previous_pay - timedelta(days=frequency)
        while (tempDate.month == previous_pay.month):
            pays_in_month += 1
            tempDate = tempDate - timedelta(days=frequency)
        # Now check forward
        tempDate = previous_pay + timedelta(days=frequency)
        while (tempDate.month == previous_pay.month):
            pays_in_month += 1
            tempDate = tempDate + timedelta(days=frequency)
    else:
        # Check for next month
        # Now check forward
        tempDate = previous_pay + timedelta(days=frequency)
        while (tempDate.month == check_date.month):
            pays_in_month += 1
            tempDate = tempDate + timedelta(days=frequency)
    return pays_in_month

def get_previous_pay_date(start_date, check_date, frequency):
    delta = check_date - start_date
    # Get the days delta...
    delta_days = delta.days
    # Now div by 14 to get cycles
    cycles = delta_days // frequency
    # Now multiply cycles by 14 to get last pay date from start
    days_to_previous_pay_from_start = cycles * frequency
    previous_pay = start_date + timedelta(days=days_to_previous_pay_from_start)
    return previous_pay

def get_rolling_nine_pay_dates(start_date, check_date, frequency):
    rolling_group = []
    previous_pay = get_previous_pay_date(start_date, check_date, frequency)
    rolling_group.append(previous_pay - timedelta(frequency * 4))
    rolling_group.append(previous_pay - timedelta(frequency * 3))
    rolling_group.append(previous_pay - timedelta(frequency * 2))
    rolling_group.append(previous_pay - timedelta(frequency))
    rolling_group.append(previous_pay)
    rolling_group.append(previous_pay + timedelta(frequency))
    rolling_group.append(previous_pay + timedelta(frequency * 2))
    rolling_group.append(previous_pay + timedelta(frequency * 3))
    rolling_group.append(previous_pay + timedelta(frequency * 4))
    return rolling_group