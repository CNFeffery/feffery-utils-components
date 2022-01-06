import feffery_utils_components as fuc
import dash
from dash.dependencies import Input, Output
from dash import html

app = dash.Dash(__name__)

app.layout = html.Div(
    [
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
    style={
        'padding': '100px'
    }
)


@app.callback(
    Output('output-demo', 'children'),
    Input('captcha-demo', 'captcha'),
    prevent_initial_call=True
)
def test(captcha):

    import time

    time.sleep(3)

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


if __name__ == '__main__':
    app.run_server(debug=True)
