import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State

import pandas as pd
import plotly.graph_objs as go
import json
import base64

# 1. Launch the application
app = dash.Dash()

# 2. Import the dataset
df = pd.read_csv('data/wheels.csv')

def encode_image(image_file):
    encoded = base64.b64encode(open(image_file, 'rb').read())
    return 'data:image/png;base64,{}'.format(encoded.decode())

# 3. Create a plotly figure
trace = go.Scatter(x = df['color'], y = df['wheels'], dy = 1,
                    mode = 'markers',
                    marker = dict(size = 15))

layout = go.Layout(title = 'Hover Plot', hovermode = 'closest')

fig = go.Figure(data = [trace], layout = layout)

# 4. Create a Dash layout
app.layout = html.Div([
                html.Div([dcc.Graph(id = 'grid-plot', figure = fig)],
                        style = {'width' : '40%', 'float' : 'left'}),
                html.Div([html.Img(id = 'hover-data', src = 'children', height = 300)],
                        style = {'paddingTop' : '30px'})
                      ])

# 5. Add callback functions
@app.callback(Output('hover-data', 'src'),
              [Input('grid-plot', 'hoverData')])     # clickData
def callback_img(X):
    wheel = hoverData['points'][0]['y']
    color = hoverData['points'][0]['x']
    path = 'data/image/'
    img_name = df[(df.wheels == wheel) & (df.color == color)]['image'].values[0]
    return encode_image(path + img_name)

# 6. Add the server clause
if __name__ == '__main__':
    app.run_server()



# hoverData['points'][0]
# : 'curveNumber', 'pointNumber', 'pointIndex', 'x', 'y', 'text'
