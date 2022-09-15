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
        '请按i键',

        fuc.FefferyKeyPress(
            id='key-press-demo',
            keys='i'
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


app.clientside_callback(
    '''(pressedTimes, children) => {
        return `${children}❤️`
    }''',
    Output('output', 'children'),
    Input('key-press-demo', 'pressedTimes'),
    State('output', 'children'),
    prevent_initial_call=True
)
if __name__ == '__main__':
    app.run(debug=True)
