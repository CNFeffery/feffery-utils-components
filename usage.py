
import dash
from dash import html
import feffery_utils_components as fuc
from dash.dependencies import Input, Output, State
import uuid

app = dash.Dash(__name__, compress=True)

app.layout = html.Div(
    [
        html.Div(
            id='guide-demo'
        ),
        html.Button(
            '触发功能引导',
            id='guide-show'
        )
    ],
    style={
        'padding': 25
    }
)


@app.callback(
    Output('guide-demo', 'children'),
    Input('guide-show', 'n_clicks'),
    prevent_initial_call=True
)
def guide_demo(nClicks):

    return fuc.FefferyGuide(
        id='guide-demo-'+str(uuid.uuid4()),
        steps=[
            {
                'selector': '#guide-show',
                'title': '这是一个功能按钮',
                'content': '这里展示了本次功能引导的第一步内容。'
            },
            {
                'targetPos': {
                    'top': 200,
                    'left': 500,
                    'width': 100,
                    'height': 50
                },
                'title': '这是自定义屏幕绝对位置锚点示例',
                'content': '这里展示了本次功能引导的第二步内容。'
            }
        ],
        localKey='guide-demo-'+str(uuid.uuid4()),
        closable=True
    )


if __name__ == '__main__':
    app.run_server(debug=True)
