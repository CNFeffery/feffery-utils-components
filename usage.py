import dash
from dash import html
import feffery_utils_components as fuc
from dash.dependencies import Input, Output, State

app = dash.Dash(__name__, compress=True)

app.layout = html.Div(
    [
        fuc.FefferyWebSocket(
            id='websocket-demo',
            socketUrl='wss://demo.piesocket.com/v3/channel_1?api_key=VCXCEuvhGcBDP7XhiJJUDvR1e1D3eiVjgZ9VRiaV&notify_self'
        )
    ],
    style={
        'padding': 25
    }
)


if __name__ == '__main__':
    app.run_server(debug=True)
