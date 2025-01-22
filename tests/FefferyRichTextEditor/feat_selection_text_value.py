if True:
    import sys

    sys.path.append('../../')
    import dash
    from dash import html
    import feffery_utils_components as fuc
    from dash.dependencies import Input, Output
    from feffery_dash_utils.style_utils import style

app = dash.Dash(__name__)

app.layout = html.Div(
    [
        fuc.FefferyRichTextEditor(id='selection-text-demo'),
        html.Div(id='selection-text-output'),
    ],
    style=style(padding=100),
)


@app.callback(
    Output('selection-text-output', 'children'),
    Input('selection-text-demo', 'selectionTextValue'),
    prevent_initial_call=True,
)
def download_file(selection_text_value):
    if selection_text_value:
        return selection_text_value
    return dash.no_update


if __name__ == '__main__':
    app.run(debug=True)
