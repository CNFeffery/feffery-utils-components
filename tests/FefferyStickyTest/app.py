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
        html.Div(
            fuc.FefferySticky(
                fuc.FefferyDiv(
                    shadow='always-shadow',
                    style={
                        'height': '100px',
                        'width': '100px',
                        'background': 'white'
                    }
                ),
                top=100,
                bottomBoundary='#sticky-boundary-target'
            ),
            id='sticky-boundary-target',
            style={
                'height': '2000px',
                'background': 'lightgrey',
                'padding': '200px 25px'
            }
        )
    ],
    style={
        'padding': '100px',
        'height': '10000px'
    }
)

if __name__ == '__main__':
    app.run(debug=True)
