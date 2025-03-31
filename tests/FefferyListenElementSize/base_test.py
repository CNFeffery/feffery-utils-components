if True:
    import sys

    sys.path.append('../../')
    import dash
    from dash import html
    import feffery_utils_components as fuc
    from dash.dependencies import Input, Output
    from feffery_dash_utils.style_utils import style

app = dash.Dash(__name__)

app.layout = html.Div(
    [
        fuc.FefferyListenElementSize(
            id='listen-element-size-demo',
            target='demo-target',
        ),
        html.Div(id='demo-target', style=style(height=300)),
    ],
    style=style(padding=100),
)


@app.callback(
    Output('demo-target', 'children'),
    Input('listen-element-size-demo', 'width'),
    Input('listen-element-size-demo', 'height'),
)
def demo(width, height):
    return f'width: {width}, height: {height}'


if __name__ == '__main__':
    app.run(debug=True)
