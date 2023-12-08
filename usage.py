
import dash
from dash import html
import feffery_utils_components as fuc
from dash.dependencies import Input, Output

app = dash.Dash(__name__, compress=True)

app.layout = html.Div(
    [

        html.Div(
            [
                fuc.FefferyFancyButton(
                    '倒计时10秒',
                    id='trigger-count-down-demo1',
                ),
                html.Div(
                    id='count-down-demo1-output'
                ),

                fuc.FefferyCountDown(
                    id='count-down-demo1'
                )
            ],
        ),
        fuc.FefferyCountUp(
            end=99999
        ),
        html.Div(
            [
                fuc.FefferyFancyButton(
                    '切换主题',
                    id='css-var-demo',
                ),
                fuc.FefferyCssVar(
                    id='css-var-demo-output'
                ),

                html.Div(
                    'FefferyCssVar示例',
                    style={
                        'background': 'var(--demo-bg-color)',
                        'color': 'var(--demo-color)',
                        'display': 'flex',
                        'justifyContent': 'center',
                        'alignItems': 'center',
                        'fontSize': '28px',
                        'transition': '0.2s',
                        'padding': '100px 150px',
                        'borderRadius': '5px'
                    }
                )
            ],
        )
    ]
)


@app.callback(
    Output('count-down-demo1', 'delay'),
    Input('trigger-count-down-demo1', 'nClicks'),
    prevent_initial_call=True
)
def countdown_demo1_trigger(nClicks):

    return 10


@app.callback(
    Output('count-down-demo1-output', 'children'),
    Input('count-down-demo1', 'countdown'),
    prevent_initial_call=True
)
def countdown_demo1_update(countdown):

    if countdown == 0:
        return

    return f'还剩{countdown}秒'


# 使用浏览器端回调以实现更丝滑的响应速度
app.clientside_callback(
    '''(nClicks) => {
        if (nClicks % 2 === 0) {
            return {
                '--demo-bg-color': 'black',
                '--demo-color': 'white'
            }
        }
        return {
            '--demo-bg-color': '#fffbe6',
            '--demo-color': 'black'
        }
    }''',
    Output('css-var-demo-output', 'cssVars'),
    Input('css-var-demo', 'nClicks')
)


if __name__ == '__main__':
    app.run_server(debug=True)
