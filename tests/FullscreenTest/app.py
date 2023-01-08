if True:
    import sys
    sys.path.append('../..')
    import dash
    from dash import html
    import feffery_utils_components as fuc
    from dash.dependencies import Input, Output, State


app = dash.Dash(__name__)

app.layout = html.Div(
    [
        html.Div(
            [
                fuc.FefferyFancyButton(
                    '全屏化',
                    id='enter-fullscreen'
                ),
                html.Br(),
                '测试' * 500
            ],
            id='target-demo',
            style={
                'border': '1px solid #292a2b',
                'background': 'white',
                'padding': '25px'
            }
        ),

        fuc.FefferyFullscreen(
            id='fullscreen-demo',
            targetId='target-demo'
        )
    ],
    style={
        'padding': '50px'
    }
)


@app.callback(
    Output('fullscreen-demo', 'isFullscreen'),
    Input('enter-fullscreen', 'nClicks'),
    State('fullscreen-demo', 'isFullscreen'),
    prevent_initial_call=True
)
def enter_fullscreen(nClicks, isFullscreen):

    return not isFullscreen


if __name__ == '__main__':
    app.run(debug=True)
