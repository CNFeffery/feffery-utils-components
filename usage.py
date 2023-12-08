
import dash
from dash import html
import feffery_utils_components as fuc

app = dash.Dash(__name__, compress=True)

app.layout = html.Div(
    [
        fuc.FefferyRgbColorPicker(
            showAlpha=True
        )
    ],
    style={
        'padding': 25
    }
)

if __name__ == '__main__':
    app.run_server(debug=True)
