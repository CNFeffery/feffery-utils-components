if True:
    import sys
    import time
    sys.path.append('../..')
    import dash
    from dash import html
    import feffery_utils_components as fuc
    from dash.dependencies import Input, Output, State


app = dash.Dash(
    __name__,
    assets_ignore='demo\.css'
)

app.layout = html.Div(
    [
        html.Span('样式测试'),
        html.Span(id='recently-status'),

        fuc.FefferyExternalCss(
            id='external-css-demo'
        ),

        html.Div(
            [
                html.Button(
                    '挂载',
                    id='load'
                ),
                html.Button(
                    '卸载',
                    id='unload'
                )
            ]
        )
    ],
    style={
        'height': '2000px'
    }
)


@app.callback(
    Output('external-css-demo', 'cssUrl'),
    [Input('load', 'n_clicks'),
     Input('unload', 'n_clicks')],
    prevent_initial_call=True
)
def demo1(*args):

    if dash.ctx.triggered_id == 'load':
        return '/assets/demo.css'

    else:
        return ''


@app.callback(
    Output('recently-status', 'children'),
    Input('external-css-demo', 'recentlyStatus')
)
def demo2(recentlyStatus):

    return recentlyStatus


if __name__ == '__main__':
    app.run(debug=True)
