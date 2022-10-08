if True:
    import sys
    import time
    sys.path.append('../..')
    import dash
    import uuid
    from dash import html, dcc
    import feffery_utils_components as fuc
    from dash.dependencies import Input, Output, State


app = dash.Dash(__name__)

app.layout = html.Div(
    [
        html.Button(
            '触发',
            id='trigger-button'
        ),

        html.Div(
            id='fancy-message-container',
            style={
                'height': '800px'
            }
        )
    ]
)


@app.callback(
    Output('fancy-message-container', 'children'),
    Input('trigger-button', 'n_clicks')
)
def demo(n_clicks):

    if n_clicks:

        return fuc.FefferyFancyMessage(
            html.Span('自定义内容测试', style={'color': 'green'}),
            type='error'
        )


if __name__ == '__main__':
    app.run(debug=True)
