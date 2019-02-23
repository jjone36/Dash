import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

import pandas as pd
import plotly.graph_objs as go

# 1. Launch the application
app = dash.Dash()

# 2. Import the dataset


# 3. Create a plotly figure


# 4. Create a Dash layout
app.layout = html.Div([
                dcc.RangeSlider(id = 'slider',
                    marks = {i: str(i) for i in range(-10, 11)},
                    min=-10, max=10, value=[-3, 4]),
                html.H2(id = 'sum-num')
                      ])

# 5. Add Callback functions
@app.callback(Output('sum-num', 'children'),
              [Input('slider', 'value')])
def update_value(value_list):
    return value_list[0] * value_list[1]

# 6. Add the server clause
if __name__ == '__main__':
    app.run_server()
