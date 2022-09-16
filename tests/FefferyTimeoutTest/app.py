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
        html.Div(
            [
                dcc.Input(
                    id='delay',
                    value=3000,
                    style={
                        'width': '200px'
                    }
                ),
                html.Button(
                    '执行',
                    id='button'
                )
            ]
        ),
        fuc.FefferyTimeout(id='timeout', delay=5000),
        html.Div(id='timeout-result')
    ],
    style={
        'height': '2000px'
    }
)


@app.callback(
    Output('timeout', 'delay'),
    Input('button', 'n_clicks'),
    State('delay', 'value')
)
def demo1(n_clicks, delay):

    if delay:
        print(int(delay))
        return int(delay)


@app.callback(
    Output('timeout-result', 'children'),
    Input('timeout', 'timeoutCount')
)
def demo2(timeoutCount):

    print(timeoutCount)

    return timeoutCount


if __name__ == '__main__':
    app.run(debug=True)
