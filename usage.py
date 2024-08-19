import dash
import json
from dash import html
from dash.dependencies import Input, Output, State
import feffery_utils_components as fuc

app = dash.Dash(__name__)

app.layout = html.Div(
    [
        html.Button('获取网络状态', id='test-button'),
        fuc.FefferyNetwork(id='network-demo'),
        html.Pre(id='output'),
    ],
    style={'padding': 50},
)


@app.callback(
    Output('output', 'children'),
    Input('test-button', 'n_clicks'),
    [
        State('network-demo', 'online'),
        State('network-demo', 'since'),
        State('network-demo', 'rtt'),
        State('network-demo', 'type'),
        State('network-demo', 'downlink'),
        State('network-demo', 'downlinkMax'),
        State('network-demo', 'saveData'),
        State('network-demo', 'effectiveType'),
    ],
)
def update_output(
    n_clicks,
    online,
    since,
    rtt,
    type,
    downlink,
    downlinkMax,
    saveData,
    effectiveType,
):
    return json.dumps(
        {
            'online': online,
            'since': since,
            'rtt': rtt,
            'type': type,
            'downlink': downlink,
            'downlinkMax': downlinkMax,
            'saveData': saveData,
            'effectiveType': effectiveType,
        },
        indent=4,
        ensure_ascii=False,
    )


if __name__ == '__main__':
    app.run(debug=True)
