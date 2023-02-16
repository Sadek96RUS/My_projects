import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import dash
from dash import html
from dash import dcc
from dash.dependencies import Input, Output
from dash import no_update

app = dash.Dash(__name__)
#app.config.supress_callback_exceptions = True
air_data = pd.read_csv('airline_data.csv')
years = [i for i in range(2005, 2021, 1)]
app.layout = html.Div(children=[html.H1('Airline Information Dashboard',
                                        style={'textAlign': 'center', 'color': '#503D36', 'font-size': 24}),
                                html.Div([
                                    html.Div([
                                        html.Div(
                                            [html.H2('Performance', style={'margin-right': '2em'})]),
                                        dcc.Dropdown(id='input-type',
                                                     options=[
                                                         {'label': 'The preformance of Airline',
                                                          'value': 'opt1'},
                                                         {'label': 'The delay',
                                                          'value': 'opt2'}
                                                     ], placeholder='Select the type',
                                                     style={'width': '80%', 'padding': '3px', 'font-size': '20px', 'text-align-last': 'center'})], style={'display': 'flex'}),
                                    html.Div([
                                        html.Div(
                                            [html.H2('Year', style={'margin-right': '2em'})]),
                                        dcc.Dropdown(id='input-year',
                                                     options=[
                                                         {'label': i, 'value': i} for i in years],
                                                     placeholder='Select the year',
                                                     style={
                                                         'width': '80%', 'padding': '3px', 'font-size': '20px', 'text-align-last': 'center'})], style={'display': 'flex'})]),

                                html.Div([], id='plot1'),
                                html.Div([
                                    html.Div([], id='plot2'),
                                    html.Div([], id='plot3')], style={'display': 'flex'}
),
    html.Div([
        html.Div([], id='plot4'),
        html.Div([], id='plot5')
    ], style={'display': 'flex'})

])


if __name__ == ('__main__'):
    app.run_server(port=9012)
