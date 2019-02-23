# https://plot.ly/python/
# https://dash.plot.ly/dash-core-components
# http://flask.pocoo.org/docs/1.0/deploying/

import dash
import dash_core_components as dcc
import dash_html_components as html

import pandas as pd
import plotly.graph_objs as go

# 1. Launch the application
app = dash.Dash()

# 2. Import the dataset
df = pd.read_csv(filename)


# 3. Create a plotly figure



# 4. Create a Dash layout
app.layout = html.Div([
                dcc.Graph(id = 'plot_id', figure = fig)
                      ])

# 5. Add callback functions


# 6. Add the server clause
if __name__ == '__main__':
    app.run_server()
