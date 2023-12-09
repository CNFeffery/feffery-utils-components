
import dash
from dash import html
import feffery_utils_components as fuc
from dash.dependencies import Input, Output

app = dash.Dash(__name__, compress=True)

app.layout = html.Div(
    [
        fuc.FefferyFancyButton(
            '执行示例',
            id='execute-js-demo'
        ),

        fuc.FefferyExecuteJs(
            id='execute-js-demo-output'
        )
    ],
    style={
        'padding': 25
    }
)


@app.callback(
    Output('execute-js-demo-output', 'jsString'),
    Input('execute-js-demo', 'nClicks'),
    prevent_initial_call=True
)
def execute_js_demo(nClicks):

    return 'alert("FefferyExecuteJs示例");'

if __name__ == '__main__':
    app.run_server(debug=True)
