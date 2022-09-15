if True:
    import sys
    import time
    sys.path.append('../..')
    import dash
    from dash import html, dcc
    import feffery_utils_components as fuc
    from dash.dependencies import Input, Output, State


app = dash.Dash(__name__)

app.layout = html.Div(
    [
        fuc.FefferyWindowSize(id='window-size-demo'),

        html.Div(id='output')
    ],
    style={
        'height': '2000px'
    }
)


@app.callback(
    Output('output', 'children'),
    [Input('window-size-demo', '_width'),
     Input('window-size-demo', '_height')]
)
def demo(_width, _height):

    return f'_width: {_width}, _height: {_height}'


if __name__ == '__main__':
    app.run(debug=True)
