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
        fuc.FefferyFormatNumber(value=1000),
        html.Br(),
        fuc.FefferyFormatNumber(
            value=1000, noGrouping=True
        ),
        html.Br(),
        *[
            fuc.FefferyFormatNumber(
                value=value, type='percent'
            )
            for value in [0, 0.25, 0.5, 0.75, 1]
        ],
        html.Br(),
        fuc.FefferyFormatNumber(
            value=1000, minimumFractionDigits=3
        ),
        html.Br(),
        fuc.FefferyFormatNumber(
            value=1000.13123321312, maximumFractionDigits=5
        ),
    ],
    style=style(padding=50),
)

if __name__ == '__main__':
    app.run(debug=True)
