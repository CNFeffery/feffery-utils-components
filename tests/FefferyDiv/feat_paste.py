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
        fuc.FefferyDiv(
            id='div-demo',
            enableEvents=['paste'],
            style=style(
                height=200,
                border='1px solid #d9d9d9',
            ),
        )
    ],
    style=style(padding=100),
)


@app.callback(
    Output('div-demo', 'children'),
    Input('div-demo', 'pasteEvent'),
    prevent_initial_call=True,
)
def demo(pasteEvent):
    return pasteEvent.get('text')


if __name__ == '__main__':
    app.run(debug=True)
