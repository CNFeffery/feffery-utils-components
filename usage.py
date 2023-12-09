
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
                dcc.Input(
                    id='timeout-demo-delay',
                    value=2000,
                    style={
                        'maxWidth': '300px'
                    }
                ),
                fuc.FefferyFancyButton(
                    '开始',
                    id='timeout-demo-start',
                    type='primary'
                )
            ]
        ),
        fuc.FefferyTimeout(
            id='timeout-demo'
        ),

        fuc.FefferyExecuteJs(
            id='timeout-demo-output'
        )
    ],
    style={
        'padding': 25
    }
)


@app.callback(
    Output('timeout-demo', 'delay'),
    Input('timeout-demo-start', 'nClicks'),
    State('timeout-demo-delay', 'value'),
    prevent_initial_call=True
)
def start_new_timeout(nClicks, value):

    if value > 0:
        return value


@app.callback(
    Output('timeout-demo-output', 'jsString'),
    Input('timeout-demo', 'timeoutCount'),
    prevent_initial_call=True
)
def after_timeout(timeoutCount):

    return 'alert(`timeoutCount=${%s}`)' % timeoutCount


if __name__ == '__main__':
    app.run_server(debug=True)
