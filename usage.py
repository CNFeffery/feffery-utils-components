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
            id='local-storage-demo-input'
        ),

        fuc.FefferyExecuteJs(
            id='local-storage-demo-trigger'
        ),

        fuc.FefferyLocalStorage(id='local-storage-demo'),

        html.Pre(id='local-storage-demo-output')
    ],
    style={
        'padding': 50
    }
)


@app.callback(
    Output('local-storage-demo-trigger', 'jsString'),
    Input('local-storage-demo-input', 'n_clicks'),
    prevent_initial_call=True
)
def trigger_local_storage_set(nClicks):

    return '''localStorage.setItem('local-storage-demo', JSON.stringify({'点击次数': % s, '当前时间': new Date(Date.now())}))''' % str(nClicks)


@app.callback(
    Output('local-storage-demo-output', 'children'),
    Input('local-storage-demo', 'data')
)
def local_storage_demo(data):

    return json.dumps(
        data,
        ensure_ascii=False,
        indent=4
    )


if __name__ == '__main__':
    app.run(debug=True)
