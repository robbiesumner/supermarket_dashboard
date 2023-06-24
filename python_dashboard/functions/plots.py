from python_dashboard.functions.getData import get_data
import plotly.express as px


def rating_graph():
    grouped_data = get_data().groupby("Filiale")["Bewertung"].mean()
    fig = px.bar(grouped_data)
    return fig


def sales_graph():
    grouped_data = get_data().groupby("Filiale")["Bruttoeinkommen"].sum()
    fig = px.bar(grouped_data)
    return fig


def payment_graph():
    grouped_data = get_data().groupby("Zahlungsart")["COGS"].count()
    fig = px.pie(grouped_data, values='COGS', names=grouped_data.index, hole=.5)
    return fig


def sales_over_time_graph(store_chosen: str or list = ""):
    sliced_data = get_data(store_chosen).groupby(['Datum']).sum().reset_index()
    fig = px.line(sliced_data, x='Datum', y='Bruttoeinkommen')
    return fig
