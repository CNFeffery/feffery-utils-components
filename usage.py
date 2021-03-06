import feffery_utils_components as fuc
import dash
from dash.dependencies import Input, Output, State
from dash import html
import uuid

app = dash.Dash(__name__)


@app.callback(
    Output('execute-js-demo-output', 'jsString'),
    Input('execute-js-demo', 'n_clicks')
)
def execute_js_demo(n_clicks):

    if n_clicks:
        return f'console.log({n_clicks});window.open("https://www.baidu.com/")'


app.layout = html.Div(
    fuc.FefferyTopProgress(
        [
            fuc.FefferyDiv(
                enableListenContextMenu=True,
                style={
                    'width': '100px',
                    'height': '100px',
                    'background': 'grey'
                }
            ),


            fuc.FefferySplit(
                [
                    fuc.FefferySplitPane(
                        fuc.FefferySplit(
                            [
                                fuc.FefferySplitPane(
                                    html.Div(
                                        'a',
                                        style={
                                            'width': '100%',
                                            'height': '100%',
                                            'border': '1px solid red'
                                        }
                                    )
                                ),
                                fuc.FefferySplitPane('b'),
                                fuc.FefferySplitPane('c'),
                            ],
                            sizes=[20, 40, 40],
                            minSize=20,
                            gutterSize=10,
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
                sizes=[20, 40, 40],
                minSize=20,
                gutterSize=3,
                # dragInterval=1,
                direction='vertical',
                style={
                    'height': '400px',
                    # 'border': '1px dashed black'
                }
            ),


            html.Div(
                [
                    html.Div(
                        [
                            html.H5(_type),
                            fuc.FefferyExtraSpinner(
                                type=_type,
                                style={
                                    'marginBottom': '25px'
                                }
                            )
                        ]
                    )
                    for _type in [
                        "ball", "swap", "bars", "grid", "wave", "push", "firework",
                        "stage", "ring", "heart", "guard", "rotate", "spiral", "pulse",
                        "swish", "sequence", "impulse", "cube", "magic", "flag", "fill",
                        "sphere", "domino", "goo", "comb", "pong", "rainbow", "hoop",
                        "flapper", "jellyfish", "trace", "classic", "whisper", "metro"
                    ]
                ],
                style={
                    'marginBottom': '100px'
                }
            ),

            fuc.FefferyScrollbars(
                html.Div(
                    '??????'*5000,
                    style={
                        'padding': '50px'
                    }
                ),
                scrollbarMaxSize=50,
                style={
                    'height': '500px',
                    'border': '1px solid black'
                }
            ),

            html.Button(
                '??????',
                id='execute-js-demo'
            ),

            fuc.FefferyExecuteJs(
                id='execute-js-demo-output',
            ),

            html.Div(
                style={
                    'height': '2000px'
                }
            ),

            html.Div(
                html.Button(
                    'scroll???',
                    id='scroll-trigger'
                )
            ),

            # ???????????????
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

            fuc.FefferyGuide(
                steps=[
                    {
                        'selector': '#step1',
                        'title': '???1???',
                        'content': '?????????1???balabalabalabala'
                    },
                    {
                        'selector': '#step2',
                        'placement': 'left-bottom',
                        'title': '???2???',
                        'content': '?????????2???balabalabalabala'
                    },
                    {
                        'selector': '#step3',
                        'title': '???3???',
                        'content': '?????????3???balabalabalabala'
                    },
                    {
                        'selector': '#test',
                        'title': '???4???',
                        'content': '?????????4???balabalabalabala'
                    },
                    {
                        'selector': '#syntax-highlighter-demo',
                        'title': '???5???',
                        'content': '?????????5???balabalabalabala'
                    }
                ],
                localKey=str(uuid.uuid4()),
                # hotspot=True,
                showPreviousBtn=True,
                closable=True,
                step=-1
            ),

            html.H2('??????1', id='step1', style={'marginBottom': '200px'}),

            html.H2('??????2', id='step2', style={
                'float': 'right', 'marginBottom': '200px'}),
            html.Hr(),

            html.H2('??????3', id='step3', style={'marginBottom': '200px'}),

            fuc.FefferyShortcutPanel(
                id='shortcut-panel-demo',
                locale='zh',
                placeholder='??????????????????...',
                theme='dark',
                data=[
                    {
                        'id': "??????",
                        'title': "????????????",
                        'hotkey': "ctrl+h",
                        'section': '??????1',
                        'handler': '() => window.open("http://www.baidu.com")'
                    },
                    {
                        'id': '??????',
                        'title': '????????????',
                        'hotkey': 'ctrl+t',
                        'section': '??????1'
                    },
                    {
                        'id': '??????1',
                        'title': '??????1',
                        'children': ['??????1-2', '??????1-1'],
                        'section': '??????2'
                    },
                    {
                        'id': '??????1-1',
                        'title': '??????1-1',
                        'parent': '??????1'
                    },
                    {
                        'id': '??????1-2',
                        'title': '??????1-2',
                        'parent': '??????1'
                    }
                ]
            ),

            fuc.FefferyCaptcha(id='captcha-demo',
                               charNum=10,
                               width=300,
                               height=100,
                               fontSize=60),
            html.Div(
                html.Em(id='output-demo')
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
            '????????????????????????',
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
