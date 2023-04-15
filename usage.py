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
        fuc.FefferyMousePosition(
            id='lmouse-position-demo'
        ),
        html.Pre(
            id='position',
            style={
                'position': 'fixed',
                'top': 25,
                'left': 25
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
    Input('lmouse-position-demo', 'position')
)
def demo(position):

    return json.dumps(
        position,
        indent=4,
        ensure_ascii=False
    )


if __name__ == '__main__':
    app.run(debug=True)
