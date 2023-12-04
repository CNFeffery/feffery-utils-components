import dash
import json
from dash import html, dcc
import feffery_utils_components as fuc
from dash.dependencies import Input, Output, State

app = dash.Dash(__name__, suppress_callback_exceptions=True)

app.layout = html.Div(
    [
        fuc.FefferyJsonViewer(
            data={
                'int示例': 999,
                'float示例': 0.999,
                'string示例': '我爱dash',
                '数组示例': [0, 1, 2, 3],
                '字典示例': {
                    'a': 1,
                    'b': 2,
                    'c': 3
                }
            }
        )
    ],
    style={
        'padding': 50
    }
)


if __name__ == '__main__':
    app.run(debug=True)
