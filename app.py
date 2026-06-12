import pandas as pd
from dash import Dash, html, dcc, callback, Output, Input
import plotly.express as px

app = Dash(__name__)

df = pd.read_csv("formatted_data.csv")
df = df.sort_values("date")

# create the header
header = html.H1(
    "Pink Morsel Visualizer",
    id="header",
    style={
        "textAlign": "center",
        "color": "white",
        "backgroundColor": "#e91e8c",
        "padding": "20px",
        "margin": "0",
        "fontFamily": "Arial",
        "letterSpacing": "2px"
    }
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
    inline=True,
    style={
        "textAlign": "center",
        "padding": "15px",
        "fontFamily": "Arial",
        "fontSize": "16px",
        "backgroundColor": "#fff0f8",
        "color": "#e91e8c"
    }
)

visualization = dcc.Graph(id="visualization")

# define the app layout
app.layout = html.Div(
    [header, radio, visualization],
    style={
        "backgroundColor": "#fff0f8",
        "minHeight": "100vh",
        "margin": "0"
    }
)

@callback(
    Output("visualization", "figure"),
    Input("region-filter", "value")
)
def update_chart(region):
    filtered = df if region == "all" else df[df["region"] == region]
    fig = px.line(filtered, x="date", y="sales", title="Pink Morsel Sales",
                  labels={"date": "Date", "sales": "Sales ($)"},
                  color_discrete_sequence=["#e91e8c"])
    fig.update_layout(
        plot_bgcolor="#fff0f8",
        paper_bgcolor="#fff0f8",
        font={"family": "Arial", "color": "#333"},
        title={"font": {"size": 20, "color": "#e91e8c"}},
    )
    return fig

if __name__ == "__main__":
    app.run(debug=True)