import dash
from dash import html
import feffery_utils_components as fuc
from dash.dependencies import Input, Output

app = dash.Dash(__name__)

app.layout = html.Div(
    [
        fuc.FefferyDiv(
            id='demo-div',
            style={
                'height': 400,
                'border': '1px solid black',
                'display': 'flex',
                'justifyContent': 'center',
                'alignItems': 'center',
            },
        )
    ],
    style={'padding': 50},
)


@app.callback(
    Output('demo-div', 'children'),
    Input('demo-div', 'isTouching'),
    prevent_initial_call=True,
)
def demo(isTouching):
    return f'isTouching: {isTouching}'


if __name__ == '__main__':
    app.run(debug=True)
