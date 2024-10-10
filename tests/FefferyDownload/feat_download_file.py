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
        html.Button('下载测试', id='download-trigger'),
        fuc.FefferyDownload(id='download-demo'),
    ],
    style=style(padding=100),
)


@app.callback(
    Output('download-demo', 'file'),
    Input('download-trigger', 'n_clicks'),
    prevent_initial_call=True,
)
def download_file(n_clicks):
    if n_clicks % 2 == 1:
        return {'url': '/_favicon.ico'}

    return {
        'url': '/_favicon.ico',
        'name': '测试',
    }


if __name__ == '__main__':
    app.run(debug=True)
