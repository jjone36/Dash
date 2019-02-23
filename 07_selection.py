import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State

import numpy as np
import pandas as pd
import plotly.graph_objs as go

# 1. Launch the application
app = dash.Dash()

# 2. Import the dataset
np.random.seed(10)

x1 = np.linspace(.1, 5, 50)
x2 = np.linspace(5.1, 10, 50)
y = np.random.randint(0, 50, 50)

df1 = pd.DataFrame({'x' : x1, 'y' : y})
df2 = pd.DataFrame({'x' : x1, 'y' : y})
df3 = pd.DataFrame({'x' : x2, 'y' : y})
df = pd.concat([df1, df2, df3])

# 3. Create a plotly figure
trace = go.Scatter(x = df.x, y = df.y, mode = 'markers',
                  mode = 'markers')

layout = go.Layout(title = 'Scatter Plot', hovermode = 'closest')

fig = go.Figure(data = [trace], layout = layout)

# 4. Create a Dash layout
app.layout = html.Div([
                html.Div([dcc.Graph(id = 'plot_id', figure = fig)],
                        style = {'width' : '30%', 'display' : 'inline-block'}),
                html.Div([html.H1(id = 'density', style = {'paddingTop' : 25})],
                        style = {'width' : '30%', 'display' : 'inline-block', 'verticalAlign' : 'top'})
                      ])

# 5. Add callback functions
@app.callback(Output('density', 'children'),
             [Input('plot_id', 'selectedData')])
def callback_image(selectedData):
    return json.dumps(selectedData, indent=2)

#def find_density(selectedData):
#    pts = len(selectedData['points'])
#    rng_or_lp = list(selectedData.keys())
#    rng_or_lp.remove('points')
#    max_x = max(selectedData[rng_or_lp[0]]['x'])
#    min_x = min(selectedData[rng_or_lp[0]]['x'])
#    max_y = max(selectedData[rng_or_lp[0]]['y'])
#    min_y = min(selectedData[rng_or_lp[0]]['y'])
#    area = (max_x-min_x)*(max_y-min_y)
#    d = pts/area
#    return 'Density = {:.2f}'.format(d)

# 6. Add the server clause
if __name__ == '__main__':
    app.run_server()
