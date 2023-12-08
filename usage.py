
import dash
from dash import html
import feffery_utils_components as fuc
from dash.dependencies import Input, Output, State

app = dash.Dash(__name__, compress=True)

app.layout = html.Div(
    [
        html.Button(
            '开启拾取',
            id='enable-eye-dropper'
        ),

        fuc.FefferyEyeDropper(
            id='eye-dropper-demo'
        ),

        html.Div(
            id='eye-dropper-demo-output',
            style={
                'width': '200px',
                'height': '200px',
                'display': 'flex',
                'alignItems': 'center',
                'justifyContent': 'center',
                'borderRadius': '5px',
                'boxShadow': '0px 0px 12px rgba(0, 0, 0, .12)',
                'transition': '0.25s'
            }
        )
    ],
    style={
        'padding': 25
    }
)


@app.callback(
    Output('eye-dropper-demo', 'enable'),
    Input('enable-eye-dropper', 'n_clicks'),
    prevent_initial_call=True
)
def enable_eye_dropper_demo(nClicks):

    return True


@app.callback(
    Output('eye-dropper-demo-output', 'style'),
    Input('eye-dropper-demo', 'color'),
    State('eye-dropper-demo-output', 'style'),
    prevent_initial_call=True
)
def eye_dropper_demo(color, old_style):

    return {
        **old_style,
        'background': color
    }


if __name__ == '__main__':
    app.run_server(debug=True)
