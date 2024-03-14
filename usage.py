import dash
import json
from dash import html
import feffery_utils_components as fuc
from dash.dependencies import Input, Output

app = dash.Dash(__name__)

app.layout = html.Div(
    [
        html.Div(
            fuc.FefferyRND(
                html.Pre(id='params'),
                defaultState={
                    'width': 400,
                    'height': 300,
                    'x': 100,
                    'y': 100
                },
                id='demo-rnd',
                bounds='parent',
                style={
                    'background': '#f0f0f0',
                    'display': 'flex',
                    'alignItems': 'center',
                    'justifyContent': 'center'
                },
                selectedStyle={
                    'border': '1px solid red'
                }
            ),
            style={
                'border': '1px solid black',
                'height': 'calc(100vh - 100px)',
                'position': 'relative'
            }
        )
    ],
    style={
        'padding': '50px 50px 0 50px'
    }
)


@app.callback(
    Output('params', 'children'),
    [Input('demo-rnd', 'position'),
     Input('demo-rnd', 'size'),
     Input('demo-rnd', 'selected')]
)
def update_params(position, size, selected):

    return json.dumps(
        dict(
            position=position,
            size=size,
            selected=selected
        ),
        indent=4,
        ensure_ascii=False
    )


if __name__ == '__main__':
    app.run(debug=True)
