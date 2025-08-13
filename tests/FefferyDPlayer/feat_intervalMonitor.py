if True:
    import sys

    sys.path.append('../../')
    import dash
    from dash import html
    import feffery_utils_components as fuc
    from dash.dependencies import Input, Output

app = dash.Dash(__name__)

app.layout = html.Div(
    [
        html.Div(
            fuc.FefferyDPlayer(
                id='player',
                intervalMonitor=True,
                video={
                    'url': 'https://d2zihajmogu5jn.cloudfront.net/sintel/master.m3u8',
                    'type': 'hls',
                },
                screenshot=True,
                style={'margin': '50px', 'width': '50%'},
            ),
            id='player-container',
        ),
        fuc.FefferyFancyButton(
            type='primary',
            id='open-button',
            children='开启间隔监听',
            style={'marginLeft': '50px'},
        ),
        fuc.FefferyFancyButton(
            type='primary',
            id='close-button',
            children='关闭间隔监听',
            style={'marginLeft': '50px'},
        ),
        html.Pre(id='output'),
    ],
    style={'padding': 50},
)


@app.callback(
    Output('player', 'intervalMonitor'),
    Input('open-button', 'nClicks'),
    prevent_initial_call=True,
)
def open_player(nClicks):
    if nClicks:
        return True
    return dash.no_update


@app.callback(
    Output('player', 'intervalMonitor', allow_duplicate=True),
    Input('close-button', 'nClicks'),
    prevent_initial_call=True,
)
def close_player(nClicks):
    if nClicks:
        return False
    return dash.no_update


@app.callback(
    Output('output', 'children'),
    Input('player', 'currentVideoInfo'),
    prevent_initial_call=True,
)
def get_player(currentVideoInfo):
    if currentVideoInfo:
        return fuc.FefferyJsonViewer(data=currentVideoInfo)
    return dash.no_update


if __name__ == '__main__':
    app.run(debug=True)
