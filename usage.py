import dash
import time
from dash import html
import feffery_utils_components as fuc
from dash.dependencies import Input, Output

app = dash.Dash(__name__)

app.layout = fuc.FefferyTopProgress(
    html.Div(
        [
            html.Button(
                '测试1',
                id='button1'
            ),
            html.Button(
                '测试2',
                id='button2'
            ),
            html.Div(
                id='demo-output'
            )
        ],
        style={
            'padding': 50
        }
    ),
    listenPropsMode='include',
    includeProps=['demo-output.children'],
    debug=True
)


@app.callback(
    Output('demo-output', 'children', allow_duplicate=True),
    Input('button1', 'n_clicks'),
    prevent_initial_call=True
)
def demo1(n_clicks):

    time.sleep(2)

    return '测试1：%s' % n_clicks


@app.callback(
    Output('demo-output', 'children', allow_duplicate=True),
    Input('button2', 'n_clicks'),
    prevent_initial_call=True
)
def demo2(n_clicks):

    time.sleep(2)

    return '测试2：%s' % n_clicks


if __name__ == '__main__':
    app.run(debug=True)
