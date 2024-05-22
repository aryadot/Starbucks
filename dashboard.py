import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px
from sqlalchemy import create_engine

# Create a connection to the SQLite database
engine = create_engine('sqlite:///starbucks_stores.db')

# Retrieve data from the SQLite database
query = "SELECT * FROM store_locations"
df = pd.read_sql(query, engine)

# Create the Dash app
app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1('Starbucks Store Locations Dashboard'),
    
    html.Div([
        dcc.Dropdown(
            id='country-dropdown',
            options=[{'label': country, 'value': country} for country in df['Country'].unique()],
            placeholder='Select a country'
        )
    ]),
    
    html.Div([
        dcc.Graph(id='map-graph'),
        dcc.Graph(id='bar-graph'),
        dcc.Graph(id='pie-graph'),
        dcc.Graph(id='heatmap-graph')
    ])
])

@app.callback(
    [Output('map-graph', 'figure'),
     Output('bar-graph', 'figure'),
     Output('pie-graph', 'figure'),
     Output('heatmap-graph', 'figure')],
    [Input('country-dropdown', 'value')]
)
def update_graphs(selected_country):
    if selected_country:
        filtered_df = df[df['Country'] == selected_country]
    else:
        filtered_df = df
    
    # Create map graph
    map_fig = px.scatter_mapbox(filtered_df, lat='Latitude', lon='Longitude', hover_name='Store Name',
                                hover_data={'City': True, 'Street Address': True}, zoom=3, height=400)
    map_fig.update_layout(mapbox_style='open-street-map', margin={'r': 0, 't': 0, 'l': 0, 'b': 0})
    
    # Create bar graph
    bar_fig = px.bar(filtered_df, x='Country', y='Store Number', height=400)
    
    # Create pie graph
    pie_fig = px.pie(filtered_df, names='Ownership Type', height=400)
    
    # Create heatmap graph
    heatmap_fig = px.density_mapbox(filtered_df, lat='Latitude', lon='Longitude', z='Store Number',
                                    radius=10, center=dict(lat=0, lon=180), zoom=0, mapbox_style='open-street-map')
    
    return map_fig, bar_fig, pie_fig, heatmap_fig

if __name__ == '__main__':
    app.run_server(debug=True)