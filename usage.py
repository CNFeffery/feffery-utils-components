
from datetime import datetime
import time
import dash
from dash import html, dcc
import feffery_utils_components as fuc
from dash.dependencies import Input, Output, State
import uuid

app = dash.Dash(__name__, compress=True)

app.layout = html.Div(
    [

        html.Div(
            [
                fuc.FefferyWheelColorPicker(
                    id='top-progress-color',
                    color='#e74c3c'
                ),
                fuc.FefferyFancyButton(
                    '触发5秒耗时回调',
                    id='top-progress-trigger-demo1',
                    type='primary'
                )
            ]
        ),
        fuc.FefferyTopProgress(
            html.Div(
                id='top-progress-trigger-demo1-output'
            ),
            id='top-progress-demo',
            listenPropsMode='exclude',
            excludeProps=['top-progress-demo.color']
        )
    ],
    style={
        'padding': 25
    }
)


@app.callback(
    Output('top-progress-demo', 'color'),
    Input('top-progress-color', 'color')
)
def top_progress_demo_update_color(color):

    return color


@app.callback(
    Output('top-progress-trigger-demo1-output', 'children'),
    Input('top-progress-trigger-demo1', 'nClicks'),
    prevent_initial_call=True
)
def top_progress_demo(nClicks):

    time.sleep(5)

    return datetime.now().strftime('%Y-%m-%d %H:%M:%S')


if __name__ == '__main__':
    app.run_server(debug=True)
