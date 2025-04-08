if True:
    import sys

    sys.path.append('../../')
    import json
    import dash
    from dash import html, dcc
    import feffery_utils_components as fuc
    from dash.dependencies import Input, Output
    from feffery_dash_utils.style_utils import style

app = dash.Dash(__name__, compress=True)

app.layout = html.Div(
    [
        fuc.FefferyRouteMatch(
            id='route-match-demo',
            pattern='/app/:page',
            updateParamsWhenMatch=False,
        ),
        dcc.Link('/app/home', href='/app/home'),
        html.Br(),
        dcc.Link('/', href='/'),
        html.Pre(id='route-match-demo-output'),
    ],
    style=style(padding=50),
)


@app.callback(
    Output('route-match-demo-output', 'children'),
    [
        Input('route-match-demo', 'match'),
        Input('route-match-demo', 'params'),
    ],
)
def demo(match, params):
    return json.dumps(
        {'match': match, 'params': params}, indent=4
    )


if __name__ == '__main__':
    app.run(debug=True)
