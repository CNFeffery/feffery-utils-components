if True:
    import sys
    sys.path.append('../..')
    import dash
    import json
    from dash import html
    import feffery_utils_components as fuc
    from dash.dependencies import Input, Output

app = dash.Dash(__name__)

app.layout = html.Div(
    [
        html.Button(
            '立即重载',
            id='reload'
        ),

        html.Button(
            '延时3秒重载',
            id='reload-delay'
        ),

        fuc.FefferyReload(
            id='reload-demo'
        ),

        fuc.FefferyReload(
            id='reload-delay-demo',
            delay=3000
        )
    ],
    style={
        'padding': '20px',
        'height': '100vh'
    }
)


@app.callback(
    Output('reload-demo', 'reload'),
    Input('reload', 'n_clicks'),
    prevent_initial_call=True
)
def reload(n_clicks):

    return True


@app.callback(
    Output('reload-delay-demo', 'reload'),
    Input('reload-delay', 'n_clicks'),
    prevent_initial_call=True
)
def reload_delay(n_clicks):

    return True


if __name__ == '__main__':
    app.run(debug=True)
