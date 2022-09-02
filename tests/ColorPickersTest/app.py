if True:
    import sys
    sys.path.append('../..')
    import dash
    import json
    from dash import html
    import feffery_utils_components as fuc
    from dash.dependencies import Input, Output

app = dash.Dash(__name__)

app.layout = html.Div(
    html.Div(
        [
            html.Div(
                [
                    html.H3(
                        'FefferyHexColorPicker'
                    ),
                    fuc.FefferyHexColorPicker(
                        id='hex-color-picker-test',
                        showAlpha=True
                    ),
                    html.Pre(id='hex-color-picker-test-output')
                ],
                style={
                    'flex': 'auto'
                }
            ),

            html.Div(
                [
                    html.H3(
                        'FefferyRgbColorPicker'
                    ),
                    fuc.FefferyRgbColorPicker(
                        id='rgb-color-picker-test'
                    ),
                    html.Pre(id='rgb-color-picker-test-output')
                ],
                style={
                    'flex': 'auto'
                }
            ),

            html.Div(
                [
                    html.H3(
                        'FefferyGithubColorPicker'
                    ),
                    fuc.FefferyGithubColorPicker(
                        id='github-color-picker-test'
                    ),
                    html.Pre(id='github-color-picker-test-output')
                ],
                style={
                    'flex': 'auto'
                }
            ),

            html.Div(
                [
                    html.H3(
                        'FefferyTwitterColorPicker'
                    ),
                    fuc.FefferyTwitterColorPicker(
                        id='twitter-color-picker-test'
                    ),
                    html.Pre(id='twitter-color-picker-test-output')
                ],
                style={
                    'flex': 'auto'
                }
            ),

            html.Div(
                [
                    html.H3(
                        'FefferyBlockColorPicker'
                    ),
                    fuc.FefferyBlockColorPicker(
                        id='block-color-picker-test',
                        color='#D9E3F0'
                    ),
                    html.Pre(id='block-color-picker-test-output')
                ],
                style={
                    'flex': 'auto'
                }
            ),

            html.Div(
                [
                    html.H3(
                        'FefferyCircleColorPicker'
                    ),
                    fuc.FefferyCircleColorPicker(
                        id='circle-color-picker-test'
                    ),
                    html.Pre(id='circle-color-picker-test-output')
                ],
                style={
                    'flex': 'auto'
                }
            ),

            html.Div(
                [
                    html.H3(
                        'FefferyWheelColorPicker'
                    ),
                    fuc.FefferyWheelColorPicker(
                        id='wheel-color-picker-test'
                    ),
                    html.Pre(id='wheel-color-picker-test-output')
                ],
                style={
                    'flex': 'auto'
                }
            )
        ],
        style={
            'padding': '30px',
            'display': 'flex',
            'flexWrap': 'wrap',
            'background': '#eff6fc',
            'justifyContent': 'center'
        }
    )
)


@app.callback(
    Output('hex-color-picker-test-output', 'children'),
    Input('hex-color-picker-test', 'color')
)
def hex_color_picker_test(color):

    if color:

        return json.dumps(
            {
                'color': color
            },
            indent=4
        )


@app.callback(
    Output('rgb-color-picker-test-output', 'children'),
    Input('rgb-color-picker-test', 'color')
)
def rgb_color_picker_test(color):

    if color:

        return json.dumps(
            {
                'color': color
            },
            indent=4
        )


@app.callback(
    Output('github-color-picker-test-output', 'children'),
    Input('github-color-picker-test', 'color')
)
def github_color_picker_test(color):

    if color:

        return json.dumps(
            {
                'color': color
            },
            indent=4
        )


@app.callback(
    Output('twitter-color-picker-test-output', 'children'),
    Input('twitter-color-picker-test', 'color')
)
def twitter_color_picker_test(color):

    if color:

        return json.dumps(
            {
                'color': color
            },
            indent=4
        )


@app.callback(
    Output('block-color-picker-test-output', 'children'),
    Input('block-color-picker-test', 'color')
)
def block_color_picker_test(color):

    if color:

        return json.dumps(
            {
                'color': color
            },
            indent=4
        )


@app.callback(
    Output('circle-color-picker-test-output', 'children'),
    Input('circle-color-picker-test', 'color')
)
def circle_color_picker_test(color):

    if color:

        return json.dumps(
            {
                'color': color
            },
            indent=4
        )


@app.callback(
    Output('wheel-color-picker-test-output', 'children'),
    Input('wheel-color-picker-test', 'color')
)
def wheel_color_picker_test(color):

    if color:

        return json.dumps(
            {
                'color': color
            },
            indent=4
        )


if __name__ == '__main__':
    app.run(debug=True)
