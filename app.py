import pandas as pd
from dash import Dash, html, dcc
import plotly.express as px

app = Dash(__name__)

df = pd.read_csv("formatted_data.csv")
df = df.sort_values("date")

fig = px.line(df, x="date", y="sales", title="Pink Morsel Sales")
visualization = dcc.Graph(
    id="visualization",
    figure=fig
)

# create the header
header = html.H1(
    "Pink Morsel Visualizer",
    id="header"
)

# define the app layout
app.layout = html.Div(
    [
        header,
        visualization
    ]
)

if __name__ == "__main__":
    app.run(debug=True)