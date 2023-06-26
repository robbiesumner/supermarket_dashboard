import plotly.express as px

from python_dashboard.functions.getData import get_data


def rating_graph():
    grouped_data = get_data().groupby("Filiale")["Bewertung"].mean()
    fig = px.bar(grouped_data, y="Bewertung", color=grouped_data.index, title="Average rating per store")
    return fig


def sales_graph():
    grouped_data = get_data().groupby("Filiale")["Bruttoeinkommen"].sum()
    fig = px.bar(grouped_data, y="Bruttoeinkommen", color=grouped_data.index, title="Sales per store")
    return fig


def payment_graph():
    grouped_data = get_data().groupby("Zahlungsart")["COGS"].count().rename("Payments")
    fig = px.pie(grouped_data, values='Payments', names=grouped_data.index, hole=.5,
                 title="Amount of transactions per payment method")

    return fig


def sales_over_time_graph(store_chosen: str or list = ""):
    sliced_data = get_data(store_chosen).groupby(['Datum']).sum().reset_index()
    fig = px.line(sliced_data, x='Datum', y='Bruttoeinkommen', title="All Sales over time")
    return fig
