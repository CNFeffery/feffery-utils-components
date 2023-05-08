import json
import dash
from dash import html, dcc
import feffery_utils_components as fuc
from dash.dependencies import Input, Output, State

app = dash.Dash(__name__)

app.layout = html.Div(
    [
        fuc.FefferyDiv(
            '测试',
            justify='center',
            align='center',
            shadow='always-shadow',
            borderRadius=6,
            style={
                'height': 200,
                'marginBottom': 50
            }
        ),

        fuc.FefferyDiv(
            shadow='always-shadow-light',
            borderRadius=6,
            style={
                'height': 200
            }
        )
    ],
    style={
        'padding': '50px 100px'
    }
)

if __name__ == '__main__':
    app.run(debug=True)
