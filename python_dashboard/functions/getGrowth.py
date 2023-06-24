import datetime

import pandas as pd

from python_dashboard.functions.getData import get_data
from python_dashboard.functions.getSalesTimeFrame import get_sales_sum_timeframe


def calculate_growth() -> float:
    """
    Calculates the growth of the last month compared to the month before
    Since there is no current data we took the latest data point as a reference point. In a real world scenario we would use the current day with as a reference point.
    :return: The growth as a float with 2 decimal places
    """
    latest_data_date = pd.to_datetime(
        get_data()["Datum"].max())  # datetime.datetime.now() This could be used in a real world scenario

    last_month = get_sales_sum_timeframe(start_date=latest_data_date - datetime.timedelta(days=30))
    month_before = get_sales_sum_timeframe(start_date=latest_data_date - datetime.timedelta(days=60),
                                           end_date=latest_data_date - datetime.timedelta(days=30))
    return round((last_month - month_before) / month_before * 100, 2)
