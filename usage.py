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
        fuc.FefferyStyle(
            rawStyle='''
.custom-right-resize-handle:hover, .custom-right-resize-handle:active {
    background: #007fd4;
    transition: 0.3s background;
}

.custom-right-resize-handle {
    transition: 0.3s background;
    width: 4px !important;
    right: -2px !important;
}
'''
        ),
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
            minWidth=200,
            maxWidth=400,
            handleClassNames={
                'right': 'custom-right-resize-handle'
            }
        )
    ],
    style={
        'height': '100vh'
    }
)

if __name__ == '__main__':
    app.run(debug=True)
