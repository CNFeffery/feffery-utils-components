if True:
    import sys
    sys.path.append('../..')
    import dash
    import json
    from dash import html, dcc
    import feffery_utils_components as fuc
    from dash.dependencies import Input, Output, State


app = dash.Dash(__name__)

app.layout = html.Div(
    [
        fuc.FefferyJsonViewer(
            id='json-viewer',
            data={
                'a': 1,
                'b': 'xxx',
                'c': [1, 2, 3],
                'd': {
                    'd1': 1,
                    'd2': 2
                },
                'e': None
            },
            theme='summerfruit:inverted',
            indent=4,
            editable=True,
            deletable=True,
            addible=True,
            style={
                # 'height': '200px',
                # 'overflowY': 'auto'
            }
        ),
        html.Pre(
            id='json-viewer-output'
        ),
        html.Span(id='nClicks')
    ],
    style={
        'height': '2000px'
    }
)


@app.callback(
    Output('json-viewer-output', 'children'),
    Input('json-viewer', 'data')
)
def sync_data(data):

    return json.dumps(
        data,
        indent=4,
        ensure_ascii=False
    )


if __name__ == '__main__':
    app.run(debug=True)
