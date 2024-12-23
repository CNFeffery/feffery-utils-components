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
        fuc.FefferyPostEventSource(
            url='https://broad-scene-1112.ploomberapp.io/stream-post',
        )
    ],
    style=style(padding=100),
)

if __name__ == '__main__':
    app.run(debug=True)
