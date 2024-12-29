if True:
    import sys

    sys.path.append('../../')
    import dash
    from dash import html
    import feffery_utils_components as fuc
    from dash.dependencies import Input, Output

app = dash.Dash(__name__)

app.layout = html.Div(
    [
        fuc.FefferyListenScroll(id='listen-scroll-demo'),
        html.Pre(
            id='listen-scroll-demo-output',
            style={
                'position': 'fixed',
                'left': '50%',
                'top': '50%',
                'transform': 'translate(-50%, -50%)',
            },
        ),
        html.Div(style={'width': 99999, 'height': 99999}),
    ]
)


app.clientside_callback(
    """( position ) => JSON.stringify(position)""",
    Output('listen-scroll-demo-output', 'children'),
    Input('listen-scroll-demo', 'position'),
)

if __name__ == '__main__':
    app.run(debug=True)
