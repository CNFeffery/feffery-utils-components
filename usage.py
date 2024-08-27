import json
import dash
import time
from dash import html
from flask import Response, abort
import feffery_utils_components as fuc
from dash.dependencies import Input, Output

app = dash.Dash(__name__)


@app.server.route('/stream')
def stream():
    def _stream():
        for i in range(999):
            time.sleep(0.5)
            yield 'data: {}\n\n'.format(time.time())

    time.sleep(3)
    abort(404)
    return Response(_stream(), mimetype='text/event-stream')


app.layout = html.Div(
    [
        fuc.FefferyEventSource(
            id='sse-demo',
            url='/stream',
        ),
        html.Pre(id='output'),
    ],
    style={'padding': 50},
)


@app.callback(
    Output('output', 'children'),
    Input('sse-demo', 'errorEvent'),
    prevent_initial_call=True,
)
def show_error(errorEvent):
    return json.dumps(errorEvent)


if __name__ == '__main__':
    app.run(debug=True)
