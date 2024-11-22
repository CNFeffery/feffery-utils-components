if True:
    import sys

    sys.path.append('../../')
    import dash
    from dash import html
    from dash.dependencies import Input
    import feffery_utils_components as fuc

app = dash.Dash(__name__)

app.layout = html.Div(
    [
        fuc.FefferyLongPress(
            id='listen-long-pressing',
            targetId='button-demo',
        ),
        html.Button('test', id='button-demo'),
    ]
)


@app.callback(
    Input('listen-long-pressing', 'isLongPressing'),
)
def demo(isLongPressing):
    print('isLongPressing: ', isLongPressing)


if __name__ == '__main__':
    app.run(debug=True)
