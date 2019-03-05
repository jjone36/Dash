# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State

import pandas as pd
import plotly.graph_objs as go


# 1. Launch the application
app = dash.Dash()

# 2. Import the dataset


# 3. Create a plotly figure


# 4. Create a Dash layout
app.layout = html.Div([
                dcc.Input(id = 'number-in', value = 1, style = {'fontSize' : 24}),
                html.Button(id = 'submit', n_clicks = 0, children = 'SUBMIT',
                            style = {'fontSize' : 25}),
                html.H1(id = 'number-out')
                      ])

# 5. Add callback functions
@app.callback(Output('number-out', 'children'),
              [Input('submit', 'n_clicks')],
              [State('number-in', 'value')])
def output(n_clicks, X):
    return X

# 5. Add the server clause
if __name__ == '__main__':
    app.run_server()
