import dash
import json
from dash import html
import feffery_utils_components as fuc
from dash.dependencies import Input, Output

app = dash.Dash(__name__)

app.layout = html.Div(
    [
        # wait-until-element-rendered模式示例
        html.Button(
            'wait-until-element-rendered模式',
            id='execute-js'
        ),
        # 控制目标元素渲染
        html.Button(
            '渲染目标元素',
            id='render-target-element'
        ),
        html.Div(
            id='execute-js-output'
        ),
        html.Div(
            id='target-element-container'
        )
    ],
    style={
        'padding': '50px 50px 0 50px'
    }
)


@app.callback(
    Output('target-element-container', 'children'),
    Input('render-target-element', 'n_clicks'),
    prevent_initial_call=True
)
def render_target_element(n_clicks):

    return html.Span(
        '我来也！',
        id='target-element'
    )


@app.callback(
    Output('execute-js-output', 'children'),
    Input('execute-js', 'n_clicks'),
    prevent_initial_call=True
)
def handle_execute_js(n_clicks):

    return fuc.FefferyExecuteJs(
        jsString="alert('目标元素出现！')",
        mode='wait-until-element-rendered',
        targetSelector='#target-element'
    )


if __name__ == '__main__':
    app.run(debug=True)
