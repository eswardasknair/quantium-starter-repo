from dash import Dash, dcc, html
import plotly.express as px
import pandas as pd

df = pd.read_csv('formatted_data.csv')
df = df.sort_values(by='date')
app = Dash(__name__)
fig = px.line(
    df, 
    x='date', 
    y='sales', 
    title='Pink Morsel Sales Before and After Price Increase'
)
fig.update_layout(
    xaxis_title="Date",
    yaxis_title="Sales ($)"
)
app.layout = html.Div(children=[
    html.H1(
        children='Pink Morsel Visualiser',
        style={'textAlign': 'center'}
    ),
    dcc.Graph(
        id='sales-line-chart',
        figure=fig
    )
])
if __name__ == '__main__':
    app.run(debug=True)