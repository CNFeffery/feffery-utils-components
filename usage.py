import json
import dash
from dash import html
import feffery_utils_components as fuc
from dash.dependencies import Input, Output, State

app = dash.Dash(
    __name__,
    suppress_callback_exceptions=True
)

app.layout = html.Div(
    [
        fuc.FefferyListenScroll(
            id='listen-scroll-demo',
            target='scroll-target-container'
        ),
        html.Pre(
            id='position',
            style={
                'position': 'fixed',
                'top': 25,
                'left': 25
            }
        ),

        html.Div(
            html.Div(
                style={
                    'width': 99999,
                    'height': 99999
                }
            ),
            id='scroll-target-container',
            style={
                'position': 'fixed',
                'width': 500,
                'height': 300,
                'overflow': 'auto',
                'top': '50%',
                'left': '20%',
                'border': '1px solid lighgrey'
            }
        )
    ],
    style={
        'padding': '50px 100px',
        'height': 99999,
        'width': 99999
    }
)


@app.callback(
    Output('position', 'children'),
    Input('listen-scroll-demo', 'position')
)
def demo(position):

    return json.dumps(
        position
    )


if __name__ == '__main__':
    app.run(debug=True)
