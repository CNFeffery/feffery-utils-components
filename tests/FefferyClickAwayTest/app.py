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
        fuc.FefferyDiv(
            id='div-demo',
            style={
                'width': '200px',
                'height': '100px',
                'background': 'lightgrey',
                'border': '1ox dashed black'
            }
        )
    ],
    style={
        'height': '2000px'
    }
)


@app.callback(
    Output('div-demo', 'children'),
    Input('div-demo', 'clickAwayCount')
)
def demo(clickAwayCount):

    return clickAwayCount


if __name__ == '__main__':
    app.run(debug=True)
