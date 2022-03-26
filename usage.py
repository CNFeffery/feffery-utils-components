import feffery_utils_components as fuc
import dash
from dash.dependencies import Input, Output, State
from dash import html
import uuid

app = dash.Dash(__name__)


app.layout = html.Div(
    fuc.FefferyTopProgress(
        [

            html.Div(
                style={
                    'height': '2000px'
                }
            ),

            html.Div(
                html.Button(
                    'scroll！',
                    id='scroll-trigger'
                )
            ),

            # 绑定滚动器
            fuc.FefferyScroll(
                id='scroll',
                duration=3000,
                smooth='easeInOutQuad',
                scrollMode='target',
                scrollTargetId='step3',
                offset=-300
            ),

            fuc.FefferyCircleColorPicker(
                color='red'
            ),

            fuc.FefferyExecuteJs(),

            fuc.FefferySplit(
                [
                    fuc.FefferySplitPane(
                        fuc.FefferySplit(
                            [
                                fuc.FefferySplitPane(
                                    html.Div(
                                        'a',
                                        style={
                                            'width': '100px',
                                            'height': '100px',
                                            'border': '1px solid red'
                                        }
                                    )
                                ),
                                fuc.FefferySplitPane('b'),
                                fuc.FefferySplitPane('c'),
                            ],
                            # defaultSizes=[20, 40, 40],
                            minSize=20,
                            gutterSize=3,
                            # dragInterval=1,
                            # direction='vertical',
                            style={
                                'height': '100%'
                            }
                        ),
                        style={
                            'height': '100%'
                        }
                    ),
                    fuc.FefferySplitPane('b'),
                    fuc.FefferySplitPane('c'),
                ],
                # defaultSizes=[20, 40, 40],
                minSize=20,
                gutterSize=3,
                # dragInterval=1,
                direction='vertical',
                style={
                    'height': '400px',
                    # 'border': '1px dashed black'
                }
            ),

            fuc.FefferyGuide(
                steps=[
                    {
                        'selector': '#step1',
                        'title': '第1步',
                        'content': '这是第1步balabalabalabala'
                    },
                    {
                        'selector': '#step2',
                        'placement': 'left-bottom',
                        'title': '第2步',
                        'content': '这是第2步balabalabalabala'
                    },
                    {
                        'selector': '#step3',
                        'title': '第3步',
                        'content': '这是第3步balabalabalabala'
                    },
                    {
                        'selector': '#test',
                        'title': '第4步',
                        'content': '这是第4步balabalabalabala'
                    },
                    {
                        'selector': '#syntax-highlighter-demo',
                        'title': '第5步',
                        'content': '这是第5步balabalabalabala'
                    }
                ],
                localKey=str(uuid.uuid4()),
                # hotspot=True,
                showPreviousBtn=True,
                closable=True,
                step=-1
            ),

            html.H2('节点1', id='step1', style={'marginBottom': '200px'}),

            html.H2('节点2', id='step2', style={
                'float': 'right', 'marginBottom': '200px'}),
            html.Hr(),

            html.H2('节点3', id='step3', style={'marginBottom': '200px'}),

            fuc.FefferyShortcutPanel(
                id='shortcut-panel-demo',
                locale='zh',
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
                id='syntax-highlighter-demo',
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


@app.callback(
    Output('scroll', 'executeScroll'),
    Input('scroll-trigger', 'n_clicks')
)
def scroll_test(n_clicks):

    if n_clicks:
        return True

    return False


if __name__ == '__main__':
    app.run_server(debug=True)
