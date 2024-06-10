import dash
import time
import random
from dash import html
from urllib.parse import unquote
import feffery_utils_components as fuc
from flask import request, Response
from dash.dependencies import Input, Output, State

app = dash.Dash(__name__)


@app.server.route('/stream-chat')
def chatgpt():
    question = request.args.get('question', '')
    question = unquote(question).strip()

    def stream():
        for s in '测试问题回复结果' + '巴拉' * 1000:
            time.sleep(random.uniform(0.05, 0.25))
            yield 'data: %s\n\n' % s

    return Response(stream(), mimetype='text/event-stream')


app.layout = html.Div(
    [
        fuc.FefferyEventSource(
            id='sse-demo',
            url='/stream-chat?question=%E4%BD%A0%E6%98%AF%E8%B0%81',
            autoReconnect=False,
        ),
        html.Div('', id='sse-demo-output'),
    ],
    style={'padding': 50},
)

app.clientside_callback(
    """(data, children) => data ? children + data : ''""",
    Output('sse-demo-output', 'children'),
    Input('sse-demo', 'data'),
    State('sse-demo-output', 'children'),
)

if __name__ == '__main__':
    app.run(debug=True)
