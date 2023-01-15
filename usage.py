import dash
import time
from datetime import datetime
from dash import html, dcc
import feffery_utils_components as fuc
from dash.dependencies import Input, Output, State

app = dash.Dash(__name__)

app.layout = html.Div(
    [
        fuc.FefferyDiv(
            '测试'*1000,
            style={
                'width': '200px',
                'maxHeight': '100px',
                'border': '1px solid #edebe9',
                'marginBottom': '25px',
                'borderRadius': '6px',
                'padding': '10px',
                'overflowY': 'auto'
            },
            shadow='always-shadow',
            scrollbar='simple'
        ),

        fuc.FefferyDiv(
            '测试'*1000,
            style={
                'width': '200px',
                'maxHeight': '100px',
                'border': '1px solid #edebe9',
                'marginBottom': '25px',
                'borderRadius': '6px',
                'padding': '10px',
                'overflowY': 'auto'
            },
            shadow='hover-shadow',
            scrollbar='simple'
        ),

        fuc.FefferyDiv(
            '测试'*1000,
            style={
                'width': '200px',
                'maxHeight': '100px',
                'border': '1px solid #edebe9',
                'marginBottom': '25px',
                'borderRadius': '6px',
                'padding': '10px',
                'overflowY': 'auto'
            },
            shadow='always-shadow',
            scrollbar='hidden'
        ),

        html.Hr(),

        fuc.FefferyDiv(
            '测试'*1000,
            className={
                'background': 'white'
            },
            style={
                'width': '200px',
                'maxHeight': '100px',
                'border': '1px solid #edebe9',
                'marginBottom': '25px',
                'borderRadius': '6px',
                'padding': '10px',
                'overflowY': 'auto'
            },
            shadow='always-shadow',
            scrollbar='simple'
        ),

        fuc.FefferyDiv(
            '测试'*1000,
            className={
                'background': 'white'
            },
            style={
                'width': '200px',
                'maxHeight': '100px',
                'border': '1px solid #edebe9',
                'marginBottom': '25px',
                'borderRadius': '6px',
                'padding': '10px',
                'overflowY': 'auto'
            },
            shadow='hover-shadow',
            scrollbar='simple'
        ),

        fuc.FefferyDiv(
            '测试'*1000,
            className={
                'background': 'white'
            },
            style={
                'width': '200px',
                'maxHeight': '100px',
                'border': '1px solid #edebe9',
                'marginBottom': '25px',
                'borderRadius': '6px',
                'padding': '10px',
                'overflowY': 'auto'
            },
            shadow='always-shadow',
            scrollbar='hidden'
        ),
    ],
    style={
        'padding': '50px'
    }
)


if __name__ == '__main__':
    app.run(debug=True)
