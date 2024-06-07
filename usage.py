import dash
import json
from dash import html
import feffery_utils_components as fuc
from dash.dependencies import Input, Output

app = dash.Dash(__name__)

app.layout = html.Div(
    [
        fuc.FefferyEventSource(
            id='sse-demo',
            url='https://sse.dev/test',
            immediate=False,
        ),
        html.Button('open', id='open'),
        html.Button('close', id='close'),
        html.Pre(id='output'),
    ]
)


@app.callback(
    Output('output', 'children'),
    [
        Input('sse-demo', 'status'),
        Input('sse-demo', 'data'),
        Input('sse-demo', 'event'),
    ],
)
def update_output(status, data, event):
    return json.dumps(
        {'status': status, 'data': data, 'event': event},
        indent=2,
        ensure_ascii=False,
    )


@app.callback(
    Output('sse-demo', 'operation'),
    [
        Input('open', 'n_clicks'),
        Input('close', 'n_clicks'),
    ],
    prevent_initial_call=True,
)
def operation(*args):
    if dash.ctx.triggered_id == 'open':
        return 'open'

    return 'close'


if __name__ == '__main__':
    app.run(debug=True)
