if True:
    import sys

    sys.path.append('../../')
    import dash
    from dash import html
    import feffery_antd_components as fac
    import feffery_utils_components as fuc
    from feffery_dash_utils.style_utils import style
    from dash.dependencies import Input, Output, State

app = dash.Dash(__name__)

app.layout = html.Div(
    [
        fuc.FefferyFullscreen(
            id='fullscreen-demo',
            targetId='fullscreen-target',
            pageFullscreen={'zIndex': 1},
        ),
        html.Div(
            fac.AntdTooltip(
                fac.AntdButton(
                    '全屏化',
                    id='toggle-fullscreen',
                    type='primary',
                ),
                title='测试',
            ),
            id='fullscreen-target',
            style={
                'height': '200px',
                'display': 'flex',
                'justifyContent': 'center',
                'alignItems': 'center',
                'background': 'white',
            },
        ),
    ],
    style=style(padding=100),
)


@app.callback(
    [
        Output('fullscreen-demo', 'isFullscreen'),
        Output('toggle-fullscreen', 'children'),
    ],
    Input('toggle-fullscreen', 'nClicks'),
    State('fullscreen-demo', 'isFullscreen'),
    prevent_initial_call=True,
)
def toggle_fullscreen(nClicks, isFullscreen):
    return [
        not isFullscreen,
        '全屏化' if isFullscreen else '退出全屏化',
    ]


if __name__ == '__main__':
    app.run(debug=True)
