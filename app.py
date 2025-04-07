import dash
from dash import dcc, html, Input, Output
import pandas as pd
import plotly.express as px

# Load and prepare the data
df = pd.read_csv("formatted_sales_data.csv")
df["date"] = pd.to_datetime(df["date"])

# Initialize the app
app = dash.Dash(__name__)

# App layout
app.layout = html.Div(style={"fontFamily": "Arial, sans-serif", "padding": "40px"}, children=[
    html.H1("📈 Pink Morsel Sales Dashboard", style={"textAlign": "center", "color": "#AA336A"}),

    html.Div([
        html.Label("Filter by Region:", style={"fontSize": "18px", "marginBottom": "10px"}),
        dcc.RadioItems(
            id="region-selector",
            options=[
                {"label": "North", "value": "north"},
                {"label": "East", "value": "east"},
                {"label": "South", "value": "south"},
                {"label": "West", "value": "west"},
                {"label": "All Regions", "value": "all"}
            ],
            value="all",
            labelStyle={"display": "inline-block", "margin-right": "15px"},
            inputStyle={"margin-right": "6px"},
            style={"marginBottom": "30px"}
        )
    ], style={"textAlign": "center"}),

    dcc.Graph(id="sales-graph")
])

# Callback to update the chart
@app.callback(
    Output("sales-graph", "figure"),
    Input("region-selector", "value")
)
def update_graph(selected_region):
    if selected_region == "all":
        filtered_df = df
    else:
        filtered_df = df[df["region"] == selected_region]

    fig = px.line(
        filtered_df,
        x="date",
        y="sales",
        color="region" if selected_region == "all" else None,
        title="Pink Morsel Sales Over Time"
    )

    # Add vertical line for price increase
    fig.add_vline(
        x=pd.to_datetime("2021-01-15"),
        line_dash="dash",
        line_color="red"
    )
    fig.add_annotation(
        x=pd.to_datetime("2021-01-15"),
        y=max(filtered_df["sales"]),
        text="Price Increase",
        showarrow=True,
        arrowhead=1
    )

    # Aesthetic tweaks
    fig.update_layout(
        xaxis_title="Date",
        yaxis_title="Sales",
        template="plotly_white",
        font=dict(family="Arial", size=14),
        title_x=0.5
    )

    return fig

# Run the server
if __name__ == "__main__":
    app.run(debug=True)
