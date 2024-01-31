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
                    id='to-parent-message-sender',
                    role='sender',
                    mode='to-parent'
                ),
                fuc.FefferyIframeMessenger(
                    id='to-child-message-receiver',
                    role='receiver',
                    mode='to-child'
                )
            ]
        ),
        html.Div(
            [
                dcc.Input(
                    id='to-parent-message',
                    style={
                        'width': 150
                    }
                ),
                html.Button(
                    '子 -> 父',
                    id='to-parent-message-send'
                )
            ]
        ),
        html.Pre(
            id='to-child-message-receive',
        )
    ],
    style={
        'padding': 50
    }
)


@app.callback(
    Output('to-parent-message-sender', 'toSendMessage'),
    Input('to-parent-message-send', 'n_clicks'),
    State('to-parent-message', 'value'),
    prevent_initial_call=True
)
def send_message_to_parent(n_clicks, value):

    return value or dash.no_update


@app.callback(
    Output('to-child-message-receive', 'children'),
    Input('to-child-message-receiver', 'recivedMessage')
)
def show_recived_message(recivedMessage):

    return f'recivedMessage: {recivedMessage}'


if __name__ == '__main__':
    app.run(debug=True, port=8051)
