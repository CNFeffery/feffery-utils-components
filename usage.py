
import dash
from dash import html
import feffery_utils_components as fuc
from dash.dependencies import Input, Output
import uuid

app = dash.Dash(__name__, compress=True)

app.layout = html.Div(
    [
        html.Div(
            [
                fuc.FefferyFancyButton(
                    '滚动至页面底部',
                    id='scroll-to-bottom-demo',
                    type='primary'
                ),
                fuc.FefferyFancyButton(
                    '滚动至距离顶部800px处',
                    id='scroll-top-offset-demo',
                    type='primary'
                ),
                fuc.FefferyFancyButton(
                    '相对当前位置向下滚动300px',
                    id='scroll-relative-offset-demo',
                    type='primary'
                ),
                fuc.FefferyFancyButton(
                    '滚动至示例元素处',
                    id='scroll-target-demo',
                    type='primary'
                )
            ]
        ),
        html.Div(
            [
                html.Div(
                    '示例目标元素',
                    id='scroll-target-element'
                ),
                fuc.FefferyFancyButton(
                    '滚动至页面顶部',
                    id='scroll-to-top-demo',
                    type='primary'
                ),
            ],
            style={
                'padding': '1400px 0 800px 0',
                'background': 'linear-gradient(180deg,#1890ff80,#fff)'
            }
        ),

        html.Div(
            id='scroll-demo-output'
        )
    ],
    style={
        'padding': 25
    }
)


@app.callback(
    Output('scroll-demo-output', 'children'),
    [Input('scroll-to-top-demo', 'nClicks'),
     Input('scroll-to-bottom-demo', 'nClicks'),
     Input('scroll-top-offset-demo', 'nClicks'),
     Input('scroll-relative-offset-demo', 'nClicks'),
     Input('scroll-target-demo', 'nClicks')],
    prevent_initial_call=True
)
def scroll_demo(*args):

    # 基于dash的上下文功能获知当前回调由谁触发
    trigger_id = dash.ctx.triggered_id

    if trigger_id == 'scroll-to-top-demo':
        return fuc.FefferyScroll(
            executeScroll=True,
            scrollMode='to-top'
        )

    elif trigger_id == 'scroll-to-bottom-demo':
        return fuc.FefferyScroll(
            executeScroll=True,
            scrollMode='to-bottom'
        )

    elif trigger_id == 'scroll-top-offset-demo':
        return fuc.FefferyScroll(
            executeScroll=True,
            scrollMode='top-offset',
            scrollTopOffset=800
        )

    elif trigger_id == 'scroll-relative-offset-demo':
        return fuc.FefferyScroll(
            executeScroll=True,
            scrollMode='relative-offset',
            scrollRelativeOffset=300
        )

    elif trigger_id == 'scroll-target-demo':
        return fuc.FefferyScroll(
            executeScroll=True,
            scrollMode='target',
            scrollTargetId='scroll-target-element'
        )


if __name__ == '__main__':
    app.run_server(debug=True)
