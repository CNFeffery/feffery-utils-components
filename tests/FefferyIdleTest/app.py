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
        fuc.FefferyIdle(id='idle-demo'),

        html.Div(id='output')
    ],
    style={
        'height': '2000px'
    }
)


@app.callback(
    Output('output', 'children'),
    Input('idle-demo', 'isIdle')
)
def demo(isIdle):

    return 'isIdle: {}'.format(isIdle)


if __name__ == '__main__':
    app.run(debug=True)
