import datetime

import pandas as pd

from python_dashboard.functions.getData import get_data


def get_sales_sum_timeframe(start_date: datetime.date = None, end_date: str = None, store_chosen: str or list = ""):
    df = get_data(store_chosen)
    df['datetime'] = pd.to_datetime(df['Datum'])

    if start_date:
        df = df[(df['datetime'] >= start_date)]
    if end_date:
        df = df[(df['datetime'] <= end_date)]
    sales_sum = df["Bruttoeinkommen"].sum()
    return round(sales_sum, 2)

