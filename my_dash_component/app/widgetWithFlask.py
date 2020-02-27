from flask import Flask
from dash.dependencies import Input, Output, State
import dash 
import dash_core_components as dcc
import dash_html_components as html

import sys
sys.path.append("..")
from my_dash_component import *


server = Flask(__name__)
app = dash.Dash(__name__, server=server)


#app.layout = html.Div(id='dash-container',
#                      children=[
#                          html.H4(children="Simple Dash Widget"),
#                          html.Div(id="output")
#                          ])
app.layout = html.Div([
    dcc.Input(id='my-id', value='initial value', type='text'),
    html.Div(id='outputDiv', style={'border': '1px solid red', "margin": 20, "padding": 10, "width": 300}),
    MyDashComponent(id="custom", label="foo", value="bar")
    ])


@app.callback(Output('outputDiv', 'children'),
              [Input("my-id", component_property="value")])
def onInput(someText):
    return someText

if __name__ == "__main__":
    app.run_server() #host='0.0.0.0', debug=True)
    
