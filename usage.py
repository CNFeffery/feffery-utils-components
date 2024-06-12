import dash
from dash import html
import feffery_utils_components as fuc

app = dash.Dash(__name__)

app.layout = html.Div(
    [
        fuc.FefferyListenScroll(
            id='global-listen-scroll-demo'
        ),
        fuc.FefferyListenScroll(
            id='local-listen-scroll-demo',
            target='local-scroll-target',
        ),
        html.Div(
            html.Div(
                style={
                    'width': 4000,
                    'height': 4000,
                }
            ),
            id='local-scroll-target',
            style={
                'width': 400,
                'height': 400,
                'overflow': 'auto',
                'position': 'fixed',
                'left': 50,
                'top': 50,
            },
        ),
    ],
    style={'padding': 50, 'height': 99999, 'width': 99999},
)

if __name__ == '__main__':
    app.run(debug=True)
