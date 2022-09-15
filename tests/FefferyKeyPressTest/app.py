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
        fuc.FefferyKeyPress(
            id='key-press-demo',
            keys='ctrl'
        ),

        html.Div(
            '',
            id='output'
        )
    ],
    style={
        'height': '2000px'
    }
)

s = 'I love liz.'


@app.callback(
    Output('output', 'children'),
    Input('key-press-demo', 'pressedTimes'),
    State('output', 'children'),
    prevent_initial_call=True
)
def demo(pressedTimes, children):

    if children != s:
        return s[:(len(children) + 1)]

    return dash.no_update


if __name__ == '__main__':
    app.run(debug=True)
