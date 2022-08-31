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
            html.H3(
                'FefferyHexColorPicker'
            ),
            fuc.FefferyHexColorPicker(
                id='hex-color-picker-test',
                showAlpha=True
            ),
            html.Pre(id='hex-color-picker-test-output'),

            html.H3(
                'FefferyRgbColorPicker'
            ),
            fuc.FefferyRgbColorPicker(
                id='rgb-color-picker-test'
            ),
            html.Pre(id='rgb-color-picker-test-output')
        ],
        style={
            'padding': '30px 0'
        }
    ),
    style={
        'width': '800px',
        'margin': '0 auto'
    }
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


if __name__ == '__main__':
    app.run(debug=True)
