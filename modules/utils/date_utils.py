from datetime import date
from dateutil.relativedelta import relativedelta

def get_target_yyyymm(months_ago=2):
    """
    Returns the year-month string (yyyy-MM) for the given number of months ago.
    """
    target_date = date.today() - relativedelta(months=months_ago)
    return target_date.strftime("%Y-%m")