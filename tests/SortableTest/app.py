if True:
    import sys
    sys.path.append('../..')
    import dash
    from dash import html
    import feffery_utils_components as fuc
    from dash.dependencies import Input, Output

app = dash.Dash(__name__)

app.layout = html.Div(
    [
        fuc.FefferySortableContainer(
            [
                fuc.FefferySortableItem(
                    html.Div(
                        f'记录{i}',
                        style={
                            'height': '32px',
                            'borderBottom': '1px solid #efefef',
                            'display': 'flex',
                            'alignItems': 'center',
                            'paddingLeft': '25px',
                            'background': 'white'
                        }
                    )
                )
                for i in range(10)
            ],
            style={
                'border': '1px solid #efefef'
            }
        )
    ],
    style={
        'paddingTop': '50px',
        'paddingBottom': '50px',
        'width': '600px',
        'margin': '0 auto'
    }
)


if __name__ == '__main__':
    app.run(debug=True)
