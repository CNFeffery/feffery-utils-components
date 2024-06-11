import dash
from dash import html
import feffery_utils_components as fuc
from dash.dependencies import Input, Output

app = dash.Dash(__name__)

app.layout = html.Div(
    [
        fuc.FefferyListenHover(
            id='listen-hover-demo',
            targetSelector='#listen-hover-target',
        ),
        html.Div(
            id='listen-hover-target',
            style={
                'width': 200,
                'height': 200,
                'background': '#d9d9d9',
            },
        ),
    ],
    style={'padding': 50},
)

app.clientside_callback(
    '(isHovering) => `isHovering: ${isHovering}`',
    Output('listen-hover-target', 'children'),
    Input('listen-hover-demo', 'isHovering'),
)

if __name__ == '__main__':
    app.run(debug=True)
