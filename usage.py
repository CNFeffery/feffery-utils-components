import feffery_utils_components as fuc
import dash
from dash.dependencies import Input, Output, State
from dash import html

app = dash.Dash(__name__)


app.layout = html.Div(
    fuc.FefferyTopProgress(
        [
            fuc.FefferyShortcutPanel(
                id='shortcut-panel-demo',
                locale='cn',
                placeholder='搜索热键功能...',
                theme='dark',
                data=[
                    {
                        'id': "主页",
                        'title': "打开主页",
                        'hotkey': "ctrl+h",
                        'section': '分组1',
                        'handler': '() => window.open("http://www.baidu.com")'
                    },
                    {
                        'id': '主题',
                        'title': '切换主题',
                        'hotkey': 'ctrl+t',
                        'section': '分组1'
                    },
                    {
                        'id': '指令1',
                        'title': '指令1',
                        'children': ['指令1-2', '指令1-1'],
                        'section': '分组2'
                    },
                    {
                        'id': '指令1-1',
                        'title': '指令1-1',
                        'parent': '指令1'
                    },
                    {
                        'id': '指令1-2',
                        'title': '指令1-2',
                        'parent': '指令1'
                    }
                ]
            ),

            fuc.FefferyPasteImage(
                id='test',
                style={
                    'height': '500px',
                    'width': '800px',
                    'marginBottom': '100px'
                }
            ),
            html.Div(id='test-output'),


            fuc.FefferyCaptcha(id='captcha-demo',
                               charNum=10,
                               width=300,
                               height=100,
                               fontSize=60),
            html.Div(
                html.Em(id='output-demo')
            ),

            fuc.FefferyWaterMark(
                content='fuc FefferyWaterMark',
                fontSize=26
            ),

            fuc.FefferySyntaxHighlighter(
                showLineNumbers=True,
                showInlineLineNumbers=True,
                codeString='''html.Div(
    [
        fac.AntdBackTop(
            containerId='back-top-container-demo',
            duration=1
        ),
        fac.AntdTitle(
            '向下滑动一段距离',
            level=4
        )
    ] + [
        html.Div(
            [
                i if i % 2 == 0 else html.Br() for i in range(200)
            ]
        )
    ],
    id='back-top-container-demo',
    style={
        'maxHeight': '500px',
        'overflowY': 'auto',
        'position': 'relative',
        'backgroundColor': 'rgba(240, 240, 240, 0.2)',
        'padding': '20px'
    }
)
''',
                language='python',
                codeStyle='coy-without-shadows'
            )
        ],
        # listenPropsMode='exclude',
        # excludeProps=['output-demo.children'],
        debug=True,
        showSpinner=False
    ),
    style={
        'padding': '100px'
    }
)


@app.callback(
    Output('output-demo', 'children'),
    Input('captcha-demo', 'captcha')
)
def test(captcha):

    import time

    # time.sleep(3)

    return captcha


@app.callback(
    Output('test-output', 'children'),
    Input('test', 'currentPastedImages')
)
def test_(currentPastedImages):

    if currentPastedImages:
        return [
            html.Img(
                src=currentPastedImage
            )
            for currentPastedImage in currentPastedImages
        ]


@app.callback(
    Output('shortcut-panel-demo', 'theme'),
    Input('shortcut-panel-demo', 'triggeredHotkey'),
    State('shortcut-panel-demo', 'theme')
)
def shotycut_panel_demo(triggeredHotkey, theme):
    print(triggeredHotkey, theme)

    return 'dark' if theme == 'light' else 'light'

if __name__ == '__main__':
    app.run_server(debug=True)
