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
        fuc.FefferyDiv(
            id='container',
            shadow='always-shadow',
            style={
                'width': '400px',
                'height': '300px',
                'borderRadius': '6px'
            }
        ),

        fuc.FefferyImagePaste(
            id='image-paste',
            disabled=True
        ),

        html.Img(
            id='image-paste-output'
        )
    ]
)


@app.callback(
    Output('image-paste-output', 'src'),
    Input('image-paste', 'imageInfo'),
    prevent_initial_call=True
)
def demo(imageInfo):

    if imageInfo:
        return imageInfo['base64']


@app.callback(
    Output('image-paste', 'disabled'),
    Input('container', 'isHovering'),
    prevent_initial_call=True
)
def control_disabled(isHovering):

    return not isHovering


if __name__ == '__main__':
    app.run(debug=True)
