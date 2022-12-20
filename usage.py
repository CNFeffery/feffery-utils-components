import dash
import time
from datetime import datetime
from dash import html, dcc
import feffery_utils_components as fuc
from dash.dependencies import Input, Output, State

app = dash.Dash(__name__)

app.layout = html.Div(
    [
        fuc.FefferyStyle(
            rawStyle='''
'''
        ),
        fuc.FefferyDiv(
            style={
                'width': '300px',
                'height': '200px',
                'border': '1px solid #e1dfdd',
                'borderRadius': '6px'
            },
            shadow='always-shadow'
        )
    ],
    style={
        'padding': '50px'
    }
)

if __name__ == '__main__':
    app.run(debug=True)
