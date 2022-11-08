import dash
from dash import html, dcc
import feffery_utils_components as fuc
from dash.dependencies import Input, Output, State

app = dash.Dash(__name__)

app.layout = html.Div(
    [
        fuc.FefferyDiv(
            id='div-demo',
            style={
                'width': '400px',
                'height': '300px',
                'border': '1px solid #d9d9d9'
            }
        ),
        html.Span(id='output')
    ],
    style={
        'padding': '50px'
    }
)

@app.callback(
    Output('output', 'children'),
    [Input('div-demo', '_width'),
    Input('div-demo', '_height')],
    prevent_initial_call=True
)
def demo(_width, _height):

    print(_width, _height)

    return f'{_width}, {_height}'

if __name__ == '__main__':
    app.run(debug=True)