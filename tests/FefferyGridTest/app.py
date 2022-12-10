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
        fuc.FefferyGrid(
            [
                fuc.FefferyGridItem(
                    str(i),
                    key=str(i),
                    style={
                        'height': '100%',
                        'display': 'flex',
                        'justifyContent': 'center',
                        'alignItems': 'center'
                    }
                )
                for i in range(10)
            ],
            layouts=[
                dict(
                    i=str(i),
                    x=i,
                    y=i+1,
                    w=1,
                    h=i+i % 2+1
                )
                for i in range(5)
            ],
            cols=5,
            rowHeight=75,
            placeholderBorderRadius='5px',
            margin=[25, 25],
            style={
                'border': '1px dashed black'
            }
        )
    ]
)


if __name__ == '__main__':
    app.run(debug=True)
