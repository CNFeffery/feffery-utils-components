import dash
from dash import html
import feffery_utils_components as fuc
from dash.dependencies import Input, Output, State

app = dash.Dash(__name__)

app.layout = html.Div(
    [
        html.Pre('普通模式'),
        fuc.FefferyDPlayer(
            video={
                'url': 'https://vjs.zencdn.net/v/oceans.mp4',
                'type': 'auto'
            },
            screenshot=True,
            style={
                'margin': '50px',
                'width': '50%'
            }
        ),
        html.Pre('MSE--hls模式'),
        html.Div(
            fuc.FefferyDPlayer(
                id='player-2',
                video={
                    'url': 'https://d2zihajmogu5jn.cloudfront.net/sintel/master.m3u8',
                    'type': 'hls'
                },
                screenshot=True,
                danmaku={
                    'isOpen': True,
                    'id': 'danmaku',
                    'api': 'https://api.prprpr.me/dplayer/',
                    'addition': ['https://api.prprpr.me/dplayer/v3/bilibili?aid=[aid]']
                },
                style={
                    'margin': '50px',
                    'width': '50%'
                }
            ),
            id='player-2-container'
        ),
        fuc.FefferyFancyButton(
            type='primary',
            id='operate-button',
            children='操作',
            style={
               'marginLeft': '50px'
            }
        ),
        html.Pre('MSE--flv模式'),
        fuc.FefferyDPlayer(
            video={
                'url': 'https://flvplayer.js.org/assets/video/weathering-with-you.flv',
                'type': 'flv'
            },
            screenshot=True,
            style={
                'margin': '50px',
                'width': '50%'
            }
        ),
        html.Pre('MSE--dash模式'),
        fuc.FefferyDPlayer(
            video={
                'url': 'https://dash.akamaized.net/dash264/TestCasesIOP33/adapatationSetSwitching/5/manifest.mpd',
                'type': 'dash'
            },
            screenshot=True,
            style={
                'margin': '50px',
                'width': '50%'
            }
        ),
        html.Pre(id='output')
    ],
    style={
        'padding': 50
    }
)

@app.callback(
    Output('player-2', 'play'),
    Input('operate-button', 'nClicks'),
    prevent_initial_call=True
)
def set_player_2(nClicks):
    if nClicks:
        return True
    return dash.no_update


@app.callback(
    Output('output', 'children'),
    Input('player-2-container', 'n_clicks'),
    State('player-2-container', 'children'),
    prevent_initial_call=True
)
def get_player_2(n_clicks, children):
    if n_clicks:
        return fuc.FefferyJsonViewer(data=children)
    return dash.no_update


if __name__ == '__main__':
    app.run(debug=True)
