import pandas as pd
import dash
from dash import dcc, html
import plotly.express as px

# Load the formatted data
df = pd.read_csv("formatted_sales_data.csv")

# Convert 'date' column to datetime type
df['date'] = pd.to_datetime(df['date'])

# Sort data by date
df = df.sort_values(by='date')

# Group by date to get total sales per day
daily_sales = df.groupby('date')['sales'].sum().reset_index()

# Create the line chart
fig = px.line(
    daily_sales,
    x='date',
    y='sales',
    title='Pink Morsel Sales Over Time',
    labels={'date': 'Date', 'sales': 'Total Sales ($)'},
)

# Add a vertical line to mark the price increase date
fig.add_shape(
    type="line",
    x0="2021-01-15",
    y0=0,
    x1="2021-01-15",
    y1=daily_sales['sales'].max(),
    line=dict(
        color="red",
        width=2,
        dash="dash",
    ),
)

# Add an annotation for clarity
fig.add_annotation(
    x="2021-01-15",
    y=daily_sales['sales'].max(),
    text="Price Increase",
    showarrow=True,
    arrowhead=1,
    ax=0,
    ay=-40
)


# Create Dash app
app = dash.Dash(__name__)
app.title = "Pink Morsel Sales Visualiser"

app.layout = html.Div(children=[
    html.H1("Pink Morsel Sales Visualiser", style={'textAlign': 'center'}),

    dcc.Graph(
        id='sales-line-chart',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run(debug=True)
