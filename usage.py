import dash
import time
from datetime import datetime
from dash import html, dcc
import feffery_utils_components as fuc
from dash.dependencies import Input, Output, State

app = dash.Dash(__name__)

app.layout = html.Div(
    [
        fuc.FefferyDeviceDetect(
            id='device-detect'
        ),
        fuc.FefferyJsonViewer(
            id='json-viewer'
        )
    ],
    style={
        'padding': '50px'
    }
)


@app.callback(
    Output('json-viewer', 'data'),
    Input('device-detect', 'deviceInfo'),
    prevent_initial_call=True
)
def demo(deviceInfo):

    return deviceInfo


if __name__ == '__main__':
    app.run(debug=True)
