import dash
from dash import html
import feffery_utils_components as fuc
from dash.dependencies import Input, Output

app = dash.Dash(__name__)

app.layout = html.Div(
    [
        fuc.FefferyDiv(
            id='demo-div',
            enableFocus=True,
            style={
                'width': 400,
                'height': 300,
                'border': '1px solid black'
            }
        )
    ],
    style={
        'padding': 50
    }
)


@app.callback(
    Output('demo-div', 'children'),
    Input('demo-div', 'isFocused')
)
def demo(isFocused):

    return f'isFocused: {isFocused}'


if __name__ == '__main__':
    app.run(debug=True)
