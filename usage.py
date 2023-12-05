import dash
from dash import html
import feffery_utils_components as fuc
from dash.dependencies import Input, Output

app = dash.Dash(__name__, compress=True)

app.layout = html.Div(
    [
        fuc.FefferyBlockColorPicker(),
        fuc.FefferyCircleColorPicker(),
        html.Button(
            '开启拾取',
            id='enable-eye-dropper'
        ),
        fuc.FefferyEyeDropper(
            id='eye-dropper-demo'
        ),
        fuc.FefferyGithubColorPicker(),
        fuc.FefferyHexColorPicker(
            id='hex-color-picker-demo',
            showAlpha=True
        ),
        fuc.FefferyRgbColorPicker(
            id='rgb-color-picker-demo',
            showAlpha=True
        ),
        fuc.FefferyTwitterColorPicker(),
        fuc.FefferyWheelColorPicker()
    ],
    style={
        'padding': 50
    }
)


@app.callback(
    Output('eye-dropper-demo', 'enable'),
    Input('enable-eye-dropper', 'n_clicks'),
    prevent_initial_call=True
)
def enable_eye_dropper_demo(nClicks):

    return True


if __name__ == '__main__':
    app.run(debug=True)
