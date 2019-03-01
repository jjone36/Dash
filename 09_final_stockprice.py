# https://plot.ly/python/
# https://dash.plot.ly/dash-core-components
# http://flask.pocoo.org/docs/1.0/deploying/

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

import pandas_datareader.data as web
from datetime import datetime
import plotly.graph_objs as go
import pandas as pd

# 1. Launch the application
app = dash.Dash()

# 2. Import the dataset
url = 'https://raw.githubusercontent.com/Pierian-Data/Plotly-Dashboards-with-Dash/master/Data/NASDAQcompanylist.csv'
nsdq = pd.read_csv('url')
nsdq.set_index('Symbol', inplace=True)

options = []
mydict = {}
for tic in nsdq.index:
    mydict['label'] = str(nsdq.iloc[tic]['Name']) + ' ' + tic
    mydict['value'] = tic
    options.append(mydict)

# 3. Create a plotly figure
trace = go.Scatter(x = [1, 2], y = [3, 1])
layout = go.Layout(title = 'Default')
fig = go.Figure(data = [trace], layout = layout)

# 4. Create a Dash layout
app.layout = html.Div([
                # Main picker
                html.H1('Stock Ticker Dashboard'),
                html.Div([
                    html.H3('Enter a stock symbol', style = {'paddingRight': '30px'}),
                    dcc.Input(id = 'picker',
                              options = options,
                              value = ['TSLA'],
                              multi = True
                ],  style={'display':'inline-block', 'verticalAlign':'top', 'width' : '30%'})
                # Add date callender
                html.Div([
                    html.H3('Select start and end dates:'),
                    dcc.DatePickerRange(id = 'picker_day',
                        min_date_allowed = datetime(2015, 1, 1),
                        max_date_allowed = datetime.today(),
                        start_date = datetime(2016, 1, 1)
                        end_date = datetime.today())
                ], style = {{'display':'inline-block'}),
                # Add button
                html.Div([
                    html.Button(id = 'btn',
                                n_clicks = 0, children = 'submit',
                                style = {'fontSize' : 25, 'marginLeft' : '30px'})
                ], style = {'display' : 'incline-block'})
                # Create the plot
                dcc.Graph(id = 'plot', fig)
                      ])

# 5. Add callback functions
@app.callback(Output('plot', 'figure'),
              [Input('btn', 'n_clicks')],
              [State('picker', 'value'),
              State('picker_day', 'start_date'),
              State('picker_day', 'end_date')])
def update(n_clicks, input, day1, day2):

    start = datetime.strptime(day1[:10], '%Y-%m-%d')
    end = datetime.strptime(day2[:10], '%Y-%m-%d')

    data = []
    for k in input:
        df = web.DataReader(k, 'iex', start, end)
        trace = go.Scatter(x = df.index, y = df['close'], name = k)
        data.append(trace)

    layout = go.Layout(title = input)
    fig = go.Figure(data = data, layout = layout)

    return fig

# 6. Add the server clause
if __name__ == '__main__':
    app.run_server(debug = True)
