
import dash
from dash import html
import feffery_utils_components as fuc
from dash.dependencies import Input, Output, State

app = dash.Dash(__name__, compress=True)

app.layout = html.Div(
    [
        fuc.FefferyFullscreen(
            id='fullscreen-demo',
            targetId='fullscreen-target'
        ),
        html.Div(
            fuc.FefferyFancyButton(
                '全屏化',
                id='toggle-fullscreen'
            ),
            id='fullscreen-target',
            style={
                'height': '200px',
                'display': 'flex',
                'justifyContent': 'center',
                'alignItems': 'center',
                'background': 'white'
            }
        )
    ],
    style={
        'padding': 25
    }
)


@app.callback(
    [Output('fullscreen-demo', 'isFullscreen'),
    Output('toggle-fullscreen', 'children')],
    Input('toggle-fullscreen', 'nClicks'),
    State('fullscreen-demo', 'isFullscreen'),
    prevent_initial_call=True
)
def toggle_fullscreen(nClicks, isFullscreen):

    return [
        not isFullscreen,
        '全屏化' if isFullscreen else '退出全屏化'
    ]


if __name__ == '__main__':
    app.run_server(debug=True)
