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
        fuc.FefferyBarcode(value='Hello Barcode!'),
        fuc.FefferyBarcode(
            value='1234',
            format='pharmacode',
            lineColor='#0aa',
            width=4,
            height=40,
            displayValue=False,
        ),
        fuc.FefferyBarcode(
            renderer='img',
            value='29012343',
            format='EAN8',
            flat=False,
        ),
    ],
    style=style(padding=100),
)


if __name__ == '__main__':
    app.run(debug=True)
