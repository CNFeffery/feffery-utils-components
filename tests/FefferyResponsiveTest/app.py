if True:
    import sys
    import json
    sys.path.append('../..')
    import dash
    from dash import html, dcc
    import feffery_utils_components as fuc
    from dash.dependencies import Input, Output, State


app = dash.Dash(__name__)

app.layout = html.Div(
    [
        fuc.FefferyResponsive(
            id='responsive-demo'
        ),
        html.Pre(id='output')
    ],
    style={
        'height': '2000px'
    }
)


@app.callback(
    Output('output', 'children'),
    Input('responsive-demo', 'responsive')
)
def demo(responsive):

    return json.dumps(
        responsive,
        indent=4,
        ensure_ascii=False
    )


if __name__ == '__main__':
    app.run(debug=True)
