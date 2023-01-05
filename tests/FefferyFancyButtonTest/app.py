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
        fuc.FefferyFancyButton(
            '按钮测试',
            id='fancy-button-demo',
            type='primary',
            ripple=True
        ),
        fuc.FefferyFancyButton(
            '按钮测试',
            type='secondary',
            ripple=True
        ),
        fuc.FefferyFancyButton(
            '按钮测试',
            type='danger',
            ripple=True
        ),
        html.Span(id='nClicks')
    ],
    style={
        'height': '2000px'
    }
)


@app.callback(
    Output('nClicks', 'children'),
    Input('fancy-button-demo', 'nClicks')
)
def demo(nClicks):

    return nClicks


if __name__ == '__main__':
    app.run(debug=True)
