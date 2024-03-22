import dash
import json
from dash import html
import feffery_utils_components as fuc
from dash.dependencies import Input, Output

app = dash.Dash(__name__)

app.layout = html.Div(
    [
        # 测试元素
        fuc.FefferyDiv(
            '测试内容',
            id='demo-target',
            shadow='always-shadow-light',
            style={
                'width': 300,
                'height': 200,
                'display': 'flex',
                'justifyContent': 'center',
                'alignItems': 'center',
                'fontSize': 18,
                'fontWeight': 'bold',
                'color': 'white',
                'background': 'linear-gradient(135deg,#17ead9,#6078ea)'
            }
        ),
        # 测试激活元素转图片
        html.Button(
            '打印',
            id='execute-screenshot'
        ),
        # 测试元素转图片组件
        fuc.FefferyDom2Image(
            id='demo-dom2image',
            scale=2
        ),
        html.Div(id='demo-dom2image-output')
    ],
    style={
        'padding': '50px 50px 0 50px'
    }
)


@app.callback(
    Output('demo-dom2image', 'targetSelector'),
    Input('execute-screenshot', 'n_clicks'),
    prevent_initial_call=True
)
def demo(n_clicks):

    return '#demo-target'


@app.callback(
    Output('demo-dom2image-output', 'children'),
    Input('demo-dom2image', 'screenshotResult'),
    prevent_initial_call=True
)
def update_result(screenshotResult):

    return [
        html.Pre(
            json.dumps(
                screenshotResult,
                ensure_ascii=False,
                indent=4
            )
        ),
        html.Img(
            src=screenshotResult['dataUrl']
        )
    ]


if __name__ == '__main__':
    app.run(debug=True)
