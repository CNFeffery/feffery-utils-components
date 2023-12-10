import dash
from dash import html
import feffery_utils_components as fuc
from dash.dependencies import Input, Output, State

app = dash.Dash(__name__, compress=True)

app.layout = html.Div(
    [
        html.Button(
            '全屏化/退出全屏',
            id='toggle-fullscreen'
        ),
        fuc.FefferyFullscreen(
            id='fullscreen-demo'
        )
    ],
    id='app-container'
)


@app.callback(
    Output('fullscreen-demo', 'isFullscreen'),
    Input('toggle-fullscreen', 'n_clicks'),
    State('fullscreen-demo', 'isFullscreen'),
    prevent_initial_call=True
)
def toggle_fullscreen_demo(n_clicks, isFullscreen):

    return not isFullscreen


if __name__ == '__main__':
    app.run_server(debug=True)
