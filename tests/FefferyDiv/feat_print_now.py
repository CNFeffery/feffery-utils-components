if True:
    import sys

    sys.path.append('../../')
    import dash
    from dash import html
    import feffery_utils_components as fuc
    from dash.dependencies import Input, Output
    from feffery_dash_utils.style_utils import style

app = dash.Dash(__name__)

app.layout = html.Div(
    [
        html.Div(
            [
                html.Button('打印区块1', id='print-block1'),
                html.Button('打印区块2', id='print-block2'),
                html.Button('打印区块3', id='print-block3'),
            ],
            style=style(marginBottom=50),
        ),
        # 示例区块1
        fuc.FefferyDiv(
            '区块1内容测试' * 100, id='div-demo-block1'
        ),
        # 示例区块2
        fuc.FefferyDiv(
            '区块2内容测试' * 100,
            id='div-demo-block2',
            style=style(color='red'),
        ),
        # 示例区块3
        fuc.FefferyDiv(
            '区块2内容测试' * 100,
            id='div-demo-block3',
            style=style(
                color='green',
                fontWeight='bold',
                fontSize=20,
                fontFamily='KaiTi',
                padding=24,
            ),
        ),
    ],
    style=style(padding=100),
)


@app.callback(
    Output('div-demo-block1', 'printNow'),
    Input('print-block1', 'n_clicks'),
    prevent_initial_call=True,
)
def print_block1(n_clicks):
    return True


@app.callback(
    Output('div-demo-block2', 'printNow'),
    Input('print-block2', 'n_clicks'),
    prevent_initial_call=True,
)
def print_block2(n_clicks):
    return True


@app.callback(
    Output('div-demo-block3', 'printNow'),
    Input('print-block3', 'n_clicks'),
    prevent_initial_call=True,
)
def print_block3(n_clicks):
    return True


if __name__ == '__main__':
    app.run(debug=True)
