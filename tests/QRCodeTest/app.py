if True:
    import sys
    sys.path.append('../..')
    import dash
    import json
    from dash import html
    import feffery_utils_components as fuc

app = dash.Dash(__name__)

app.layout = html.Div(
    [
        fuc.FefferyQRCode(
            size=256,
            value='https://fac.feffery.tech/'
        ),

        fuc.FefferyQRCode(
            size=256,
            value='https://fac.feffery.tech/',
            imageSettings={
                'src': 'https://fac.feffery.tech/assets/imgs/fac-logo.svg',
                'height': 60,
                'width': 60
            }
        ),
    ],
    style={
        'width': '600px',
        'paddingTop': '50px',
        'margin': '0 auto',
        'display': 'flex',
        'flexDirection': 'column',
        'alignItems': 'center',
        'gap': '25px'
    }
)


if __name__ == '__main__':
    app.run(debug=True)
