from dash import Dash, dcc, html, Input, Output
import plotly.express as px
import pandas as pd

df = pd.read_csv('formatted_data.csv')
df = df.sort_values(by='date')

app = Dash(__name__)

app.layout = html.Div(style={'backgroundColor': '#f7f7f7', 'padding': '40px', 'fontFamily': 'Arial'}, children=[
    html.H1(
        "Pink Morsel Visualiser", 
        style={'textAlign': 'center', 'color': '#d4244b'}
    ),
    
    html.Div([
        dcc.RadioItems(
            id='region-picker',
            options=[
                {'label': ' North ', 'value': 'north'},
                {'label': ' East ', 'value': 'east'},
                {'label': ' South ', 'value': 'south'},
                {'label': ' West ', 'value': 'west'},
                {'label': ' All ', 'value': 'all'}
            ],
            value='all',
            inline=True
        )
    ], style={'textAlign': 'center', 'fontSize': '18px', 'marginBottom': '30px'}),
    
    dcc.Graph(id='sales-chart')
])

@app.callback(
    Output('sales-chart', 'figure'),
    Input('region-picker', 'value')
)
def update_chart(region):
    if region == 'all':
        filtered_df = df
    else:
        filtered_df = df[df['region'] == region]
        
    fig = px.line(
        filtered_df, 
        x='date', 
        y='sales', 
        title='Sales Data by Region',
        color_discrete_sequence=['#d4244b']
    )
    
    fig.update_layout(
        paper_bgcolor='#f7f7f7',
        plot_bgcolor='#ffffff'
    )
    
    return fig

if __name__ == '__main__':
    app.run(debug=True)