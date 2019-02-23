import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

import numpy as np
import pandas as pd
import json
import plotly.graph_objs as go

# 1. Launch the application
app = dash.Dash()

# 2. Import the dataset
df = pd.read_csv('mpg.csv')
# adding jitter to year data
df['year'] = np.random.randint(-4, 5, len(df)) * .1 + df['model_year']


# 3. Create a plotly figure
# figure 1
trace_1 = go.Scatter(x = df['year']+1900, y = df['mpg'],
                   text = df['name'],
                   hoverinfo = 'text',
                   mode = 'markers')
layout_1 = go.Layout(title = 'MPG Data',
                  xaxis = dict(title = 'Model Year'),
                  yaxis = dict(title = 'MPG'),
                  hovermode = 'closest')
fig_1 = go.Figure(data = [trace_1], layout = layout_1)

# figure 2
trace_2 = go.Scatter(x = [0, 1], y = [0, 1], mode = 'lines')
layout_2 = go.Layout(title = 'Sub plot',
                    margin = {'l' : 0})
fig_2 = go.Figure(data = [trace_2], layout = layout_2)


# 4. Create a Dash layout
app.layout = html.Div([
                html.Div([dcc.Graph(id = 'plot_1', figure = fig_1)],
                        style = {'width' : '50%', 'display' : 'incline-block'}),
                html.Div([dcc.Graph(id = 'plot_2', figure = fig_2)],
                        style = {'width' : '20%', 'display' : 'incline-block'}),
                html.Div([dcc.Markdown(id = 'markdown')],
                        style = {'width' : '20%', 'display' : 'incline-block'})
                      ])

# 5. Add callback functions
# callback for plot 2
@app.callback(Output('plot_2', 'figure'),
              [Input('plot_1', 'hoverData')])
def update_figure(input_data):
    # grab the hover point
    idx = input_data['points'][0]['pointIndex']
    # update figure 2
    trace_2 = go.Scatter(x = [0, 1],
                        y = [0, 60/df.iloc[idx]['acceleration']],
                        mode = 'lines',
                        line = {'width' : 3*df.iloc[idx]['cylinders']})
    layout_2 = go.Layout(title = df.iloc[idx]['name'],
                        yaxis = {'range' : [0, 60/df.iloc[idx]['acceleration'].min()]},
                        margin = {'l' : 0})
    fig_2 = go.Figure(data = [trace_2], layout = layout_2)
    return fig_2

# callback for markdown
@app.callback(Output('markdown', 'children'),
              [Input('plot_1', 'hoverData')])
def update_markdown(input_data):
    # grab the hover point
    idx = input_data['points'][0]['pointIndex']
    report = """
            {} cylinders
            {}cc displacement
            """.format(df.iloc[idx]['cylinders'],
                       df.iloc[idx]['displacement'])
    return report

# 6. Add the server clause
if __name__ == '__main__':
    app.run_server()
