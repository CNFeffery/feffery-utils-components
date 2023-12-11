import dash
from dash import html
import feffery_utils_components as fuc
from dash.dependencies import Input, Output, State

app = dash.Dash(__name__, compress=True)

app.layout = html.Div(
    [
        html.Button(
            '进入全屏',
            id='toggle-fullscreen'
        ),
        fuc.FefferyFullscreen(
            id='fullscreen-demo',
            isFullscreen=False
        )
    ],
    style={
        'padding': 50
    }
)


@app.callback(
    [Output('toggle-fullscreen', 'children'),
     Output('fullscreen-demo', 'isFullscreen')],
    [Input('toggle-fullscreen', 'n_clicks'),
     Input('fullscreen-demo', 'isFullscreen')],
    prevent_initial_call=True
)
def handle_fullscreen_change(n_clicks, isFullscreen):

    if dash.ctx.triggered_id == 'toggle-fullscreen':

        return [
            '退出全屏' if not isFullscreen else '进入全屏',
            not isFullscreen
        ]

    return [
        '退出全屏' if isFullscreen else '进入全屏',
        dash.no_update
    ]


if __name__ == '__main__':
    app.run_server(debug=True)
