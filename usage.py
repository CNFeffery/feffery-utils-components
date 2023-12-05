import dash
import json
from dash import html, dcc
import feffery_utils_components as fuc
from dash.dependencies import Input, Output, State

app = dash.Dash(__name__, suppress_callback_exceptions=True)

app.layout = html.Div(
    [
        fuc.FefferyResizable(
            html.Div(
                '示例内容',
                style={
                    'display': 'flex',
                    'height': '100%',
                    'justifyContent': 'center',
                    'alignItems': 'center',
                    'background': '#dee2e6'
                }
            ),
            defaultSize={
                'width': 200,
                'height': 200
            }
        )
    ],
    style={
        'padding': 50
    }
)


if __name__ == '__main__':
    app.run(debug=True)
