if True:
    import sys
    sys.path.append('../..')
    import dash
    from dash import html
    import feffery_utils_components as fuc
    from dash.dependencies import Input, Output


app = dash.Dash(__name__)

app.layout = html.Div(
    [
        fuc.FefferyInViewport(
            html.Div(
                style={
                    'height': '200px',
                    'width': '200px',
                    'border': '1px solid red'
                }
            ),
            id='in-viewport-demo',
            threshold=0.5
        ),

        html.Span(
            id='in-viewport-demo-status',
            style={
                'position': 'fixed',
                'top': '25px',
                'right': '25px'
            }
        )
    ],
    style={
        'height': '2000px'
    }
)


@app.callback(
    Output('in-viewport-demo-status', 'children'),
    Input('in-viewport-demo', 'inViewport')
)
def check_in_viewport(inViewport):
    return 'In viewport: {}'.format(inViewport)


if __name__ == '__main__':
    app.run(debug=True)
