import dash
from dash import html
import feffery_antd_charts as fact
import feffery_utils_components as fuc
from dash.dependencies import Input, Output, MATCH

app = dash.Dash(__name__)

app.layout = html.Div(
    [
        fuc.FefferyVirtualList(
            [
                html.Div(f'测试列表{i}')
                for i in range(50000)
            ],
            height=300,
            itemHeight=25
        ),
        *[
            fuc.FefferyLazyLoad(
                html.Div(
                    id={
                        'type': 'container',
                        'index': i
                    },
                    style={
                        'height': '400px',
                        'overflowWrap': 'break-word',
                        'marginBottom': '20px',
                        'border': '1px solid black'
                    }
                ),
                id={
                    'type': 'lazy-load-container',
                    'index': i
                },
                height=400,
                throttle=0
            )
            for i in range(20)
        ]
    ],
    style={
        'width': '800px',
        'margin': '0 auto'
    }
)


@app.callback(
    Output(
        {
            'type': 'container',
            'index': MATCH
        },
        'children'
    ),
    Input(
        {
            'type': 'lazy-load-container',
            'index': MATCH
        },
        'visible'
    ),
    prevent_initiall_call=True
)
def lazy_load_container_callback(visible):

    if visible:
        return fact.AntdPie(
            data=[
                {
                    'type': '分类一',
                            'value': 27,
                },
                {
                    'type': '分类二',
                            'value': 25,
                },
                {
                    'type': '分类三',
                            'value': 18,
                },
                {
                    'type': '分类四',
                            'value': 15,
                },
                {
                    'type': '分类五',
                            'value': 10,
                },
                {
                    'type': '其他',
                            'value': 5,
                },
            ],
            angleField='value',
            colorField='type',
            radius=0.9,
            label={
                'type': 'inner',
                        'offset': '-30%',
                        'style': {
                            'fontSize': 36,
                            'textAlign': 'center'
                        },
                'formatter': {
                            'func': '({ percent }) => `${(percent * 100).toFixed(0)}%`'
                        }
            }
        )

    return dash.no_update


if __name__ == '__main__':
    app.run(debug=True)
