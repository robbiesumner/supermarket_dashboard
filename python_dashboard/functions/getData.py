import pandas as pd


def get_data(store_chosen: str or list = ""):
    if store_chosen:
        df = pd.read_csv("data/supermarket_sales.csv")
        if type(store_chosen) == list:
            df = df[df['Filiale'].isin(store_chosen)]
            if df.empty:
                df = pd.read_csv("data/supermarket_sales.csv")
            return df
        if type(store_chosen) == str:
            df = df[df['Filiale'] == store_chosen]
            if df.empty:
                df = pd.read_csv("data/supermarket_sales.csv")
            return df
    df = pd.read_csv("data/supermarket_sales.csv")
    return df
