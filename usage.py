import json
import dash
import time
from flask import request
from dash import html, dcc
import feffery_utils_components as fuc
from dash.dependencies import Input, Output, State

app = dash.Dash(__name__)

app.layout = html.Div(
    [
        fuc.FefferyResizable(
            html.Div(
                '测试',
                style={
                    'height': '100%',
                    'background': '#f8f9fa'
                }
            ),
            direction=['right'],
            defaultSize={
                'height': '100%',
                'width': 300
            },
            minWidth=100
        )
    ],
    style={
        'height': '100vh'
    }
)

if __name__ == '__main__':
    app.run(debug=True)
