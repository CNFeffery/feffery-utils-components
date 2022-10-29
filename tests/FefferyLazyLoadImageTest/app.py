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
        html.Div(
            [
                i,
                fuc.FefferyLazyLoadImage(
                    src=f'https://joeschmoe.io/api/v1/random?index={i}',
                    height=200,
                    threshold=200
                )
            ],
        )
        for i in range(100)
    ],
    style={
        'height': '2000px'
    }
)

if __name__ == '__main__':
    app.run(debug=True)
