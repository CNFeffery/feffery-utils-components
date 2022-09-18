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
        fuc.FefferyCountDown(
            id='count-down-demo',
            interval=2
        ),
        html.Button(
            '设置10秒倒计时',
            id='set-10s-count-down'
        ),
        html.Div(id='count-down-output')
    ],
    style={
        'height': '2000px'
    }
)


@app.callback(
    Output('count-down-demo', 'delay'),
    Input('set-10s-count-down', 'n_clicks')
)
def demo1(n_clicks):

    if n_clicks:
        return 10


@app.callback(
    Output('count-down-output', 'children'),
    Input('count-down-demo', 'countdown')
)
def demo2(countdown):

    print(countdown)

    return countdown


if __name__ == '__main__':
    app.run(debug=True)
