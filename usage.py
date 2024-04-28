import dash
import time
import json
from dash import html, Patch
from datetime import datetime
import feffery_utils_components as fuc
from dash.exceptions import PreventUpdate
from dash.dependencies import Input, Output, ALL
from flask import jsonify, request, abort, Response

app = dash.Dash(__name__)


@app.server.route('/get-demo')
def get_demo():
    # 获取全部请求参数
    params = dict(request.args)

    if params.get('timeout'):
        time.sleep(int(params['timeout']) + 1)

    return jsonify(
        {
            '当前时间': datetime.now().strftime(
                '%Y-%m-%d %H:%M:%S'
            ),
            '请求参数': params,
        }
    )


@app.server.route('/get-error-demo')
def get_error_demo():
    abort(Response('请求错误', 400))


@app.server.route('/post-demo', methods=['POST'])
def post_demo():
    # 获取请求发送的数据
    data = request.json

    return jsonify(
        {
            '当前时间': datetime.now().strftime(
                '%Y-%m-%d %H:%M:%S'
            ),
            '携带数据': data,
        }
    )


app.layout = html.Div(
    [
        *[
            html.Button(
                value,
                id={
                    'type': 'execute-request',
                    'index': value,
                },
            )
            for value in [
                'GET请求',
                'GET请求错误',
                'POST请求',
                'GET超时请求',
            ]
        ],
        fuc.FefferyHttpRequests(id='demo-http-requests'),
        html.Pre([None, None], id='request-result'),
    ],
    style={'padding': 50},
)


@app.callback(
    Output('demo-http-requests', 'requestConfig'),
    Input(
        {
            'type': 'execute-request',
            'index': ALL,
        },
        'n_clicks',
    ),
    prevent_initial_call=True,
)
def execute_new_request(n_clicks):
    if dash.ctx.triggered_id['index'] == 'GET请求':
        return {
            'url': '/get-demo',
            'params': {
                '参数1': 1,
                '参数2': 'a',
                '参数3': 3.22,
                '参数4': [1, 2],
            },
        }

    elif dash.ctx.triggered_id['index'] == 'GET请求错误':
        return {
            'url': '/get-error-demo',
        }

    elif dash.ctx.triggered_id['index'] == 'POST请求':
        return {
            'url': '/post-demo',
            'method': 'post',
            'data': {
                '参数1': 1,
                '参数2': 'a',
                '参数3': 3.22,
                '参数4': [1, 2],
            },
        }

    elif dash.ctx.triggered_id['index'] == 'GET超时请求':
        return {
            'url': '/get-demo',
            'timeout': 3 * 1000,
            'params': {'timeout': 3},
        }

    raise PreventUpdate


@app.callback(
    Output('request-result', 'children'),
    [
        Input('demo-http-requests', 'responseResult'),
        Input('demo-http-requests', 'status'),
    ],
    prevent_initial_call=True,
)
def display_request_result(result, status):
    p = Patch()

    p[0] = status + '\n'
    p[1] = json.dumps(result, indent=4, ensure_ascii=False)

    return p


if __name__ == '__main__':
    app.run(debug=True)
