
import dash
from dash import html
import feffery_utils_components as fuc
from dash.dependencies import Input, Output

app = dash.Dash(__name__, compress=True)

app.layout = html.Div(
    [
        fuc.FefferyDeviceDetect(
            id='device-detect'
        ),

        fuc.FefferyJsonViewer(
            id='device-detect-output'
        )
    ],
    style={
        'padding': 25
    }
)


@app.callback(
    Output('device-detect-output', 'data'),
    Input('device-detect', 'deviceInfo')
)
def device_detect_demo(deviceInfo):

    return deviceInfo


if __name__ == '__main__':
    app.run_server(debug=True)
