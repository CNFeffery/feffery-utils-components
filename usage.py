import json
import uuid
import dash
import time
from flask import request
from dash import html, dcc
import feffery_utils_components as fuc
from dash.dependencies import Input, Output, State

app = dash.Dash(__name__)

app.layout = html.Div(
    [
        fuc.FefferyFancyNotification(
            '操作成功，页面即将自动刷新',
            type='success',
            autoClose=1000 * 30,
            position='top-right',
            closable=False,
            closeOnClick=False,
            draggable=False,
            containerId='container1'
        ),

        fuc.FefferyFancyNotification(
            '操作成功，页面即将自动刷新',
            type='success',
            autoClose=1000 * 30,
            position='top-left',
            closable=False,
            closeOnClick=False,
            draggable=False,
            containerId='container2'
        ),

        html.Button(
            '触发',
            id='create-new'
        ),
        html.Div(
            id='notification-output-container'
        )
    ],
    style={
        'height': '100vh'
    }
)


@app.callback(
    Output('notification-output-container', 'children'),
    Input('create-new', 'n_clicks'),
    prevent_initial_call=True
)
def create_new(n_clicks):

    return fuc.FefferyFancyNotification(
        '操作成功，页面即将自动刷新',
        type='success',
        autoClose=2000,
        position='bottom-right',
        closable=False,
        closeOnClick=False,
        draggable=False,
        style={
            'bottom': 0
        },
        containerId='container3'
    )


if __name__ == '__main__':
    app.run(debug=True)
