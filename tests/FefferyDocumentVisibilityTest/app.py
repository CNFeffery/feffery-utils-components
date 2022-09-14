if True:
    import sys
    import time
    sys.path.append('../..')
    import dash
    from dash import html
    import feffery_utils_components as fuc
    from dash.dependencies import Input, Output, State


app = dash.Dash(__name__)

app.layout = html.Div(
    [
        fuc.FefferyDocumentVisibility(
            id='document-visibility-demo'
        ),
        html.Div(
            [],
            id='output'
        )
    ],
    style={
        'height': '2000px'
    }
)


@app.callback(
    Output('output', 'children'),
    Input('document-visibility-demo', 'documentVisibility'),
    State('output', 'children')
)
def demo(documentVisibility, children):

    return [
        *children,
        html.Div(
            'documentVisibility: {}, {}'.format(
                documentVisibility, time.time()
            )
        )
    ]


if __name__ == '__main__':
    app.run(debug=True)
