import dash
from dash import html
import feffery_utils_components as fuc
from dash.dependencies import Input, Output, State

app = dash.Dash(__name__)

app.layout = html.Div(
    [
        fuc.FefferyDPlayer(
            video={
                'url': 'https://vjs.zencdn.net/v/oceans.mp4',
                'type': 'auto'
            },
            screenshot=True,
            style={
                'marginBottom': '20px'
            }
        ),
        fuc.FefferyDPlayer(
            video={
                'url': 'https://d2zihajmogu5jn.cloudfront.net/sintel/master.m3u8',
                'type': 'hls'
            },
            screenshot=True
        ),
        html.Pre(id='output')
    ],
    style={
        'padding': 50
    }
)


if __name__ == '__main__':
    app.run(debug=True)
