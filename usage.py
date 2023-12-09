
import dash
from dash import html, dcc
import feffery_utils_components as fuc
from dash.dependencies import Input, Output
import uuid

app = dash.Dash(__name__, compress=True)

app.layout = html.Div(
    [
        dcc.Input(
            id='set-title-demo',
            placeholder='请输入新title信息',
            style={
                'maxWidth': '200px'
            }
        ),

        fuc.FefferySetTitle(
            id='set-title-demo-output'
        )
    ],
    style={
        'padding': 25
    }
)


@app.callback(
    Output('set-title-demo-output', 'title'),
    Input('set-title-demo', 'value'),
    prevent_initial_call=True
)
def set_title_demo(value):

    return value or dash.no_update


if __name__ == '__main__':
    app.run_server(debug=True)
