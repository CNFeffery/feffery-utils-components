import json
import dash
import time
from flask import request
from dash import html, dcc
import feffery_utils_components as fuc
from dash.dependencies import Input, Output, State

app = dash.Dash(__name__)

app.layout = html.Div(
    [
        html.Button(
            '更新cookie',
            id='update-cookie'
        ),
        fuc.FefferyCookie(
            id='cookie-basic-demo',
            cookieKey='feffery-cookie-basic-demo',
            # defaultValue='I~love~dash!',
            # defaultValue='I+love+dash!',
            expires=5
        ),
        html.Pre(id='current-cookie')
    ],
    style={
        'padding': '50px 100px'
    }
)


@app.callback(
    Output('cookie-basic-demo', 'value'),
    Input('update-cookie', 'n_clicks'),
    prevent_initial_call=True
)
def manual_update_cookie(n_clicks):

    print(n_clicks)

    return str(int(time.time()))


@app.callback(
    Output('current-cookie', 'children'),
    Input('cookie-basic-demo', 'value')
)
def update_cookie(value):
    return json.dumps(
        value,
        indent=4
    )


if __name__ == '__main__':
    app.run(debug=True)
