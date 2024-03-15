import dash
import json
from dash import html
import feffery_utils_components as fuc
from dash.dependencies import Input, Output

app = dash.Dash(__name__)

app.layout = html.Div(
    [
        fuc.FefferyDebugGuardian()
    ],
    style={
        'padding': '50px 50px 0 50px'
    }
)


if __name__ == '__main__':
    app.run(debug=True)
