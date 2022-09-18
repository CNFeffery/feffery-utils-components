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
        html.Button(
            '刷新',
            id='refresh-demo'
        ),
        fuc.FefferyCaptcha(
            id='captcha-demo'
        ),
        html.Div(id='current-captcha')
    ],
    style={
        'height': '2000px'
    }
)


@app.callback(
    Output('captcha-demo', 'refresh'),
    Input('refresh-demo', 'n_clicks')
)
def demo1(n_clicks):

    return bool(n_clicks)


@app.callback(
    Output('current-captcha', 'children'),
    Input('captcha-demo', 'captcha')
)
def demo2(captcha):

    return captcha


if __name__ == '__main__':
    app.run(debug=True)
