if True:
    import sys

    sys.path.append('../../../')
    import dash
    from dash import html
    import feffery_utils_components as fuc
    from dash.dependencies import Input, Output, State
    from feffery_dash_utils.style_utils import style

app = dash.Dash(__name__)

app.layout = html.Div(
    [
        html.Button('打开文档', id='open-doc'),
        html.Button('关闭文档', id='close-doc'),
        fuc.FefferyDocDialog(
            id='doc-layout',
            fallbackUrl='https://fac.feffery.tech/',
            docUrls={
                '/AntdButton': 'https://fac.feffery.tech/AntdButton',
                '/AntdFloatButton': 'https://fac.feffery.tech/AntdFloatButton',
            },
        ),
    ],
    style=style(padding=50),
)


@app.callback(
    Output('doc-layout', 'visible'),
    [Input('open-doc', 'n_clicks'),
    Input('close-doc', 'n_clicks')],
    State('doc-layout', 'closeTimestamp'),
    prevent_initial_call=True,
)
def open_doc(open, close, closeTimestamp):
    triggered_id = dash.callback_context.triggered_id
    print(closeTimestamp)
    if triggered_id == 'open-doc':
        return True
    elif triggered_id == 'close-doc':
        return False
    return dash.no_update


if __name__ == '__main__':
    app.run(debug=True)
