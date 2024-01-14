import dash
from dash import html
import feffery_utils_components as fuc
from dash.dependencies import Input, Output, State
import os
from flask import request, send_file

app = dash.Dash(__name__, compress=True)

app.layout = html.Div(
    [
        fuc.FefferyBirdsBackground(
            html.Div(
                'Birds 3d背景效果',
                style={
                    'color': 'white',
                    'padding': '35%',
                    'fontSize': '55px'
                }
            ),
            id='birds-background',
            minHeight=600,
            style={
                'height': '100vh'
            }
        )
    ]
)


if __name__ == '__main__':
    app.run_server(debug=True)
