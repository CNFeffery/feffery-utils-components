
import dash
from dash import html
import feffery_utils_components as fuc
from dash.dependencies import Input, Output
import uuid

app = dash.Dash(__name__, compress=True)

app.layout = html.Div(
    [
        fuc.FefferyFancyButton(
            '立即重载',
            id='trigger-reload-demo',
            type='primary'
        ),
        fuc.FefferyReload(
            id='trigger-reload-demo-output'
        ),
    ],
    style={
        'padding': 25
    }
)


@app.callback(
    Output('trigger-reload-demo-output', 'reload'),
    Input('trigger-reload-demo', 'nClicks'),
    prevent_initial_call=True
)
def reload_demo(nClicks):

    return True


if __name__ == '__main__':
    app.run_server(debug=True)
