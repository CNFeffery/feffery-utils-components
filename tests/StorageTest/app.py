if True:
    import sys
    sys.path.append('../..')
    import dash
    import json
    import random
    from dash import html, dcc
    import feffery_utils_components as fuc
    from dash.dependencies import Input, Output, State


app = dash.Dash(__name__)

app.layout = html.Div(
    [
        html.Button(
            '更新数据',
            id='update-data'
        ),
        fuc.FefferySessionStorage(
            id='session-demo'
        ),
        html.Pre(id='session-demo-output')
    ]
)


@app.callback(
    Output('session-demo', 'data'),
    Input('update-data', 'n_clicks')
)
def update_date(n_clicks):

    return {
        'a': random.randint(0, 99999)
    }


@app.callback(
    Output('session-demo-output', 'children'),
    Input('session-demo', 'data'),
    prevent_initial_call=True
)
def session_demo(data):

    return json.dumps(
        data,
        ensure_ascii=False,
        indent=4
    )


if __name__ == '__main__':
    app.run(debug=True)
