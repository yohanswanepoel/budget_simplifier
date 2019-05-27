from datetime import datetime
from datetime import timedelta

def fortnightly_cycles_current_month(start_date):
    currentDate = datetime.datetime.now()
    while (start_date + timedelta(14) < currentDate):
        pass
    pass
