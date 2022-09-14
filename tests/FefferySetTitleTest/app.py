if True:
    import sys
    import time
    sys.path.append('../..')
    import dash
    from dash import html, dcc
    import feffery_utils_components as fuc
    from dash.dependencies import Input, Output, State


app = dash.Dash(__name__, update_title=None)

app.title = 'title测试'

app.layout = html.Div(
    [
        fuc.FefferySetTitle(
            id='set-title-demo'
        ),
        dcc.Input(
            id='title-input',
            style={
                'width': '250px'
            }
        )
    ],
    style={
        'height': '2000px'
    }
)


@app.callback(
    Output('set-title-demo', 'title'),
    Input('title-input', 'value')
)
def demo(value):

    return value


if __name__ == '__main__':
    app.run(debug=True)
