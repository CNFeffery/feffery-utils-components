if True:
    import sys
    import time
    sys.path.append('../..')
    import dash
    from dash import html, dcc
    import feffery_utils_components as fuc
    from dash.dependencies import Input, Output, State


app = dash.Dash(__name__)

app.layout = html.Div(
    [
        fuc.FefferyMotion(
            [
                fuc.FefferyFancyButton(
                    '测试'
                )
            ],
            style={
                'width': '200px',
                'height': '200px',
                'borderRadius': '200px',
                'background': '#c7e0f4',
                'display': 'flex',
                'justifyContent': 'center',
                'alignItems': 'center'
            },
            # initial={
            #     'x': 0,
            #     'scale': 1
            # },
            animate={
                'x': [400, 0, 400],
                'scale': [1.5, 1, 1.5],
                'rotate': [360, 0, 360],
                'borderRadius': [0, 200, 0],
                'skew': ['15deg, 15deg', '-15deg, -15deg', '15deg, 15deg'],
                'background': ['#004578', '#c7e0f4', '#004578']
            },
            # whileHover={'scale': 1.1},
            # whileTap={'scale': 0.9},
            transition={
                # 'type': 'spring',
                'duration': 3,
                'repeat': 'infinity',
                'ease': 'easeInOut'
            }
        )
    ],
    style={
        'padding': '200px'
    }
)


if __name__ == '__main__':
    app.run(debug=True)
