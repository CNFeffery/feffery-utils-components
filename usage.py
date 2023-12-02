import dash
import json
from dash import html, dcc
import feffery_utils_components as fuc
from dash.dependencies import Input, Output, State

app = dash.Dash(__name__, suppress_callback_exceptions=True)

app.layout = html.Div(
    [
        dcc.Location(id='url'),

        # 根据url来生成不同角色的通信器
        html.Div(id='tab-messager-role')
    ],
    style={
        'padding': 50
    }
)


@app.callback(
    Output('tab-messager-role', 'children'),
    Input('url', 'pathname')
)
def generate_tab_messager(pathname):

    if pathname == '/':
        # 生成发信者
        return [
            fuc.FefferySetTitle(
                title='发信者示例'
            ),
            html.Button(
                '发消息',
                id='send-message'
            ),
            fuc.FefferyTabMessenger(
                id='demo-sender',
                role='sender',
                targetUrl='/receiver',
                targetWindowFeatures='left=0,top=0,width=800,height=500,menubar=no,toolbar=no,location=no,status=no,resizable=yes,scrollbars=no'
            )
        ]

    elif pathname == '/receiver':
        # 生成收信者
        return [
            fuc.FefferySetTitle(
                title='收信者示例'
            ),
            fuc.FefferyTabMessenger(
                id='demo-receiver',
                role='receiver'
            ),
            html.Pre(id='recived-message')
        ]


@app.callback(
    Output('demo-sender', 'toSendMessage'),
    Input('send-message', 'n_clicks'),
    prevent_initial_call=True
)
def send_new_message(n_clicks):

    return f'n_clicks: {n_clicks}'


@app.callback(
    Output('recived-message', 'children'),
    Input('demo-receiver', 'recivedMessage'),
    prevent_initial_call=True
)
def show_recived_message(recivedMessage):

    return json.dumps(
        dict(
            recivedMessage=recivedMessage
        ),
        indent=4,
        ensure_ascii=False
    )


if __name__ == '__main__':
    app.run(debug=True)
