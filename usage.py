import dash
import json
from dash import html
import feffery_utils_components as fuc
from dash.dependencies import Input, Output

app = dash.Dash(__name__, suppress_callback_exceptions=True)

app.layout = html.Div(
    [
        html.Button(
            '执行示例js代码',
            id='session-storage-demo-input'
        ),

        fuc.FefferyExecuteJs(
            id='session-storage-demo-trigger'
        ),

        fuc.FefferySessionStorage(id='session-storage-demo', initialSync=True),

        html.Pre(id='session-storage-demo-output')
    ],
    style={
        'padding': 50
    }
)


@app.callback(
    Output('session-storage-demo-trigger', 'jsString'),
    Input('session-storage-demo-input', 'n_clicks'),
    prevent_initial_call=True
)
def trigger_session_storage_set(nClicks):

    return '''sessionStorage.setItem('session-storage-demo', JSON.stringify({'点击次数': % s, '当前时间': new Date(Date.now())}))''' % str(nClicks)


@app.callback(
    Output('session-storage-demo-output', 'children'),
    Input('session-storage-demo', 'data')
)
def session_storage_demo(data):

    return json.dumps(
        data,
        ensure_ascii=False,
        indent=4
    )


if __name__ == '__main__':
    app.run(debug=True)
