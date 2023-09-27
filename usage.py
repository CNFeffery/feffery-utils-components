import dash
import json
from dash import html
import feffery_utils_components.alias as fuc
from dash.dependencies import Input, Output

app = dash.Dash(__name__)

app.layout = html.Div(
    [
        fuc.Div(
            # wheelEventStrategy='internally-only',
            style={
                'height': 400,
                'background': '#f0f0f0'
            }
        ),
    ],
    style={
        'padding': '50px 50px 10000px 50px'
    }
)

if __name__ == '__main__':
    app.run(debug=True)
