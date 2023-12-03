import dash
import json
from dash import html, dcc
import feffery_utils_components as fuc
from dash.dependencies import Input, Output, State

app = dash.Dash(__name__, suppress_callback_exceptions=True, compress=True)

app.layout = html.Div(
    [
        fuc.FefferyCaptcha()
    ],
    style={
        'padding': 50
    }
)


if __name__ == '__main__':
    app.run(debug=True)
