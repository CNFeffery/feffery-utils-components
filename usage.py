import dash
import json
from dash import html
import feffery_utils_components as fuc
from dash.dependencies import Input, Output

app = dash.Dash(__name__)

app.layout = html.Div(
    [
        # default模式示例
        html.Button(
            'default模式',
            id='execute-js'
        ),
        html.Div(
            id='execute-js-output'
        )
    ],
    style={
        'padding': '50px 50px 0 50px'
    }
)


@app.callback(
    Output('execute-js-output', 'children'),
    Input('execute-js', 'n_clicks'),
    prevent_initial_call=True
)
def handle_execute_js(n_clicks):

    return fuc.FefferyExecuteJs(
        jsString='alert("default模式测试")'
    )


if __name__ == '__main__':
    app.run(debug=True)
