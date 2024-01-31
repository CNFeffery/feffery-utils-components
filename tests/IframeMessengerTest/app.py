if True:
    import sys
    sys.path.append('../..')
    import dash
    from dash import html, dcc
    import feffery_utils_components as fuc
    from dash.dependencies import Input, Output, State

app = dash.Dash(__name__, suppress_callback_exceptions=True)

app.layout = html.Div(
    [
        html.Div(
            [
                fuc.FefferyIframeMessenger(
                    id='to-child-message-sender',
                    role='sender',
                    mode='to-child',
                    targetIframeId='iframe-demo'
                ),
                fuc.FefferyIframeMessenger(
                    id='to-parent-message-receiver',
                    role='receiver',
                    mode='to-parent',
                    targetIframeId='iframe-demo'
                )
            ]
        ),
        html.Div(
            [
                dcc.Input(
                    id='to-child-message',
                    style={
                        'width': 150
                    }
                ),
                html.Button(
                    '父 -> 子',
                    id='to-child-message-send'
                )
            ]
        ),
        html.Pre(
            id='to-parent-message-receive',
        ),
        html.Iframe(
            id='iframe-demo',
            src='http://127.0.0.1:8051',
            style={
                'width': '100%',
                'height': 500,
                'border': '1px solid #bfbfbf'
            }
        )
    ],
    style={
        'padding': 50
    }
)


@app.callback(
    Output('to-child-message-sender', 'toSendMessage'),
    Input('to-child-message-send', 'n_clicks'),
    State('to-child-message', 'value'),
    prevent_initial_call=True
)
def send_message_to_child(n_clicks, value):

    return value or dash.no_update


@app.callback(
    Output('to-parent-message-receive', 'children'),
    Input('to-parent-message-receiver', 'recivedMessage')
)
def show_recived_message(recivedMessage):

    return f'recivedMessage: {recivedMessage}'


if __name__ == '__main__':
    app.run(debug=True)
