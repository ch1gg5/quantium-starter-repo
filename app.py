import pandas as pd
from dash import Dash, html, dcc, callback, Output, Input
import plotly.express as px

app = Dash(__name__)

df = pd.read_csv("formatted_data.csv")
df = df.sort_values("date")

# create the header
header = html.H1(
    "Pink Morsel Visualizer",
    id="header"
)

# create the radio button
radio = dcc.RadioItems(
    id="region-filter",
    options=[
        {"label": "All", "value": "all"},
        {"label": "North", "value": "north"},
        {"label": "East", "value": "east"},
        {"label": "South", "value": "south"},
        {"label": "West", "value": "west"},
    ],
    value="all",
    inline=True
)

visualization = dcc.Graph(id="visualization")

# define the app layout
app.layout = html.Div(
    [
        header,
        radio,
        visualization
    ]
)

@callback(
    Output("visualization", "figure"),
    Input("region-filter", "value")
)
def update_chart(region):
    filtered = df if region == "all" else df[df["region"] == region]
    fig = px.line(filtered, x="date", y="sales", title="Pink Morsel Sales",
                  labels={"date": "Date", "sales": "Sales ($)"})
    return fig

if __name__ == "__main__":
    app.run(debug=True)