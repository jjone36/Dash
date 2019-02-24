####################### Plotly
# https://plot.ly/python/
# https://dash.plot.ly/dash-core-components
# https://www.kaggle.com/pavanraj159/telecom-customer-churn-prediction

### notebook mode
#from plotly.offline import init_notebook_mode, iplot
#init_notebook_mode(connected=True)

import plotly
import plotly.offline as pyo
import plotly.graph_objs as go

trace = go.Scatter(x = df.X, y = df.Y,
                   mode = 'markers',
                   marker = dict(size = 10,
                                color = 'rgba(51, 204, 153, .7)',
                                symbol = 'pentagon',
                                line = {'width':1}))

layout = go.Layout(title = 'Item Plot',
                   xaxis = dict(title = 'X-values',
                                range = [-100, 100],
                                titlefont=dict(family='Arial, sans-serif',
                                                size=18,
                                                color='lightgrey')),
                   yaxis = dict(title = 'Y-values',
                                range = [-100, 100],
                                titlefont=dict(family='Arial, sans-serif',
                                                size=18,
                                                color='lightgrey')),
                   hovermode = 'closest')

fig = go.Figure(data = [trace], layout = layout)
pyo.plot(data, filename = 'plot.html')

# Bubble
trace = go.Scatter(x = df.X, y = df.Y,
                   mode = 'markers',
                   marker = dict(size = df.Z*3,
                                color = df.W,
                                showscale = True))

####################### line plot
trace = go.Scatter(x = df.X, y = df.Y,
                   mode = 'lines',
                   line = dict(width = 3))

####################### Bar plot
trace = go.Bar(x = df.X, y = df.Y,
               marker = dict(line = {'width' : .5,
                                     'color' : 'black'}))
layout = go.Layout(title = 'barchart', barmode = 'stack')

####################### Box plot
trace = go.Box(y = df.Y,
               boxpoints = 'all',
               jitter = .3, pointpos = -1)
pyo.plot(data, filename = 'box1.html')

####################### Histogram
trace = go.Histogram(x = df.X,
                    xbins = dict(start = 0, end = 25),
                    histnorm = 'percent',
                    marker = {line = {width : .5, color : 'black'}}, opacity = .6)

####################### Distplot
import plotly.figure_factory as ff
hist_data = [x1, x2, x3]
group_labels = ['X1', 'X2', 'X3']
fig = ff.create_distplot(hist_data, group_labels,
                         bin_size = [.1, .3, .2])

####################### Pie plot
labs = df.X.value_counts().keys().tolist()
vals = df.Y.value_counts().values.tolist()
trace = go.Pie(labels = labs, values = vals, hole = .4)

####################### 3D Scatter
trace = go.Scatter3d(x = df.X, y = df.Y, z = df.Z,
                    mode = 'markers',
                    marker = dict(size = 12, color = z, opacity = .5))
layout = go.Layout(margin = dict(l = 0, r = 0, b = 0, t = 0))


####################### Polar plot
r = df.X.values.tolist()
theta = df.Y.tolist()
trace = go.Scatterpolar(r = r, theta = theta,
                        fill  = "toself",
                        mode = "markers+lines",
                        marker = dict(size = 5))

####################### Maps
import shapely
import shapefile
from plotly.figure_factory._county_choropleth import create_choropleth
import geopandas

colorscale = ["#171c42","#223f78","#1267b2","#4590c4","#8cb5c9","#b6bed5","#dab2be",
"#d79d8b","#c46852","#a63329","#701b20","#3c0911"]

values = df.TOT_POP.tolist()
fips = df.FIPS.tolist()

fig = create_choropleth(scope = scope, values = values, fips = fips,
                        round_legend_values = True,
                        # show_state_data = True,
                        simplify_county = 0,
                        simplify_state = 0,
                        county_outline = {'color': 'rgb(15, 15, 55)', 'width': .5},
                        state_outline = {'width' : .5},
                        legend_title = 'Population Per Country')
iplot(fig, filename = 'Choropleth Map')
