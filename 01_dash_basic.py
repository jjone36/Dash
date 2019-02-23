# https://plot.ly/python/
# https://dash.plot.ly/dash-core-components
# -*- coding: utf-8 -*-

import dash
import dash_core_components as dcc
import dash_html_components as html

import numpy as np
import pandas as pd
import plotly.graph_objs as go

# 1. Launch the application
app = dash.Dash()

# 2. Import the dataset
df = pd.read_csv('mpg.csv')

# 3. Create a plotly figure
trace_1 = go.Scatter(x = , y = ,
                    text = df['name'],
                    hoverinfo = 'text',
                    mode = 'markers',
                    marker = dict(size = 10,
                                 color = 'rgba(51, 204, 153, .7)',
                                 symbol = 'pentagon',
                                 line = {'width':1}))

trace_2 = go.Scatter(x = , y = ,
                    text = df['name'],
                    hoverinfo = 'text',
                    mode = 'markers',
                    marker = dict(size = 10,
                                 color = 'rgba(51, 204, 153, .7)',
                                 symbol = 'pentagon',
                                 line = {'width':1}))

layout = go.Layout(title = 'MPG Scatter Plot',
                   xaxis = dict(title = 'X-values',
                                titlefont=dict(family='Arial, sans-serif',
                                                size=18,
                                                color='lightgrey')),
                   yaxis = dict(title = 'Y-values',
                                titlefont=dict(family='Arial, sans-serif',
                                                size=18,
                                                color='lightgrey')),
                   hovermode = 'closest')

fig = go.Figure(data = [trace_1, trace_2], layout = layout)

# 4. Create a Dash layout
app.layout = html.Div([
                dcc.Graph(id = 'plot_id', figure = fig)
                      ])

# 5. Add callback functions


# 6. Add the server clause
if __name__ == '__main__':
    app.run_server()
