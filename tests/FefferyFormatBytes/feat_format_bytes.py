if True:
    import sys

    sys.path.append('../../')
    import dash
    from dash import html
    import feffery_utils_components as fuc
    from feffery_dash_utils.style_utils import style

app = dash.Dash(__name__)

app.layout = html.Div(
    [
        fuc.FefferyFormatBytes(value=1000),
        html.Br(),
        *[
            fuc.FefferyFormatBytes(value=value)
            for value in [12, 1200, 1200000, 1200000000]
        ],
        html.Br(),
        *[
            fuc.FefferyFormatBytes(value=value, unit='bit')
            for value in [12, 1200, 1200000, 1200000000]
        ],
    ],
    style=style(padding=50),
)

if __name__ == '__main__':
    app.run(debug=True)
