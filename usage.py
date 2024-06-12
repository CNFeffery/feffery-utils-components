import dash
from dash import html
import feffery_utils_components as fuc
from dash.dependencies import Input, Output

app = dash.Dash(__name__)

app.layout = html.Div(
    [
        html.Div(
            id='target-element',
            style={
                'width': '20vw',
                'height': '20vh',
                'border': '1px solid black',
            },
        ),
        fuc.FefferyListenElementSize(
            id='listen-element-size-demo',
            target='target-element',
        ),
    ],
    style={'padding': 50, 'height': 99999, 'width': 99999},
)

app.clientside_callback(
    """(width, height) => `width: ${width}px; height: ${height}px`""",
    Output('target-element', 'children'),
    Input('listen-element-size-demo', 'width'),
    Input('listen-element-size-demo', 'height'),
)

if __name__ == '__main__':
    app.run(debug=True)
