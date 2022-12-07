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
        fuc.FefferyShadowDom(
            [
                fuc.FefferyStyle(
                    rawStyle='''
.div-demo {
    width: 200px;
    height: 200px;
    background: black;
}
'''
                ),
                html.Div(
                    className='div-demo'
                )
            ]
        ),

        fuc.FefferyShadowDom(
            [
                fuc.FefferyStyle(
                    rawStyle='''
.div-demo {
    width: 200px;
    height: 200px;
    background: grey;
}
'''
                ),
                html.Div(
                    className='div-demo'
                )
            ]
        )
    ]
)


if __name__ == '__main__':
    app.run(debug=True)
