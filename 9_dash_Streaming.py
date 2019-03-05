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
                html.H1(id = 'text'),
                dcc.Interval(id = 'interval',
                            interval = 2000,  # 2sec
                            n_intervals = 0)
                    ])

# 5. Add callback functions
@app.callback(Output('text', 'children'),
             [Input('interval', 'n_intervals')])
def update(n):
    return "Refreshes {} times".format(n)

# 5. Add the server clause
if __name__ == '__main__':
    app.run_server()
