
import dash
from dash import html
import feffery_utils_components as fuc
from dash.dependencies import Input, Output

app = dash.Dash(__name__, compress=True)

app.layout = html.Div(
    [
        fuc.FefferyFancyButton(
            '挂载party.js',
            id='mount-js'
        ),
        fuc.FefferyFancyButton(
            '点我试试',
            id='effect-when-mount'
        ),
        fuc.FefferyExternalJs(
            id='external-js-demo'
        ),
        fuc.FefferyExecuteJs(
            id='execute-party-effect'
        )
    ],
    style={
        'padding': 25
    }
)


@app.callback(
    [Output('external-js-demo', 'jsUrl'),
     Output('execute-party-effect', 'jsString')],
    Input('mount-js', 'nClicks'),
    prevent_initial_call=True
)
def external_js_demo(nClicks):

    if nClicks and nClicks == 1:
        return [
            'https://fastly.jsdelivr.net/npm/party-js@latest/bundle/party.min.js',
            '''
document.querySelector("#effect-when-mount").addEventListener("click", function (e) {
    party.confetti(this);
});
'''
        ]

    return dash.no_update


if __name__ == '__main__':
    app.run_server(debug=True)
