if True:
    import sys

    sys.path.append('../../')
    import dash
    from dash import html
    import feffery_utils_components as fuc
    from feffery_dash_utils.style_utils import style
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
                        'alignItems': 'center',
                    },
                )
                for i in range(10)
            ],
            id='grid-demo',
            layouts=[
                dict(
                    i=str(i),
                    x=i,
                    y=i + 1,
                    w=1,
                    h=i + i % 2 + 1,
                )
                for i in range(5)
            ],
            cols=5,
            rowHeight=75,
            placeholderBorderRadius='5px',
            margin=[25, 25],
            style={'border': '1px dashed #e1dfdd'},
            closable=True,
            draggerStyle={
                
            }
        )
    ],
    style=style(padding=50),
)


@app.callback(
    [
        Output('grid-demo', 'children'),
        Output('grid-demo', 'layouts'),
    ],
    Input('grid-demo', 'closeEvent'),
    [
        State('grid-demo', 'children'),
        State('grid-demo', 'layouts'),
    ],
    prevent_initial_call=True,
)
def handle_item_close(closeEvent, children, layouts):
    return [
        [
            child
            for child in children
            if child['props']['key'] != closeEvent['key']
        ],
        [
            item
            for item in layouts
            if item['i'] != closeEvent['key']
        ],
    ]


if __name__ == '__main__':
    app.run(debug=True)
