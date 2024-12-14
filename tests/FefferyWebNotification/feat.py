if True:
    import sys

    sys.path.append('../../')
    import uuid
    import dash
    from dash import html
    import feffery_utils_components as fuc
    from dash.dependencies import Input, Output
    from feffery_dash_utils.style_utils import style

app = dash.Dash(__name__)

app.layout = html.Div(
    [
        html.Button('新的通知', id='new-web-notification'),
        fuc.FefferyWebNotification(
            id='web-notification-demo',
        ),
    ],
    style=style(padding=100),
)


@app.callback(
    Output('web-notification-demo', 'message'),
    Input('new-web-notification', 'n_clicks'),
    prevent_initial_call=True,
)
def demo(n_clicks):
    return '通知测试' + str(uuid.uuid4())


if __name__ == '__main__':
    app.run(debug=True)
