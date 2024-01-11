import dash, json
from dash import html
import feffery_utils_components as fuc
from dash.dependencies import Input, Output, State
import os
from flask import request, send_file

app = dash.Dash(__name__, compress=True)

app.layout = html.Div(
    [
        fuc.FefferyTiltHover(
            html.Div(
                html.Div(
                    'Feffery Tilt Hover 👀',
                    style={
                        'padding': '45% 10%',
                        'fontSize': '22px',
                        'fontWeight': 'bold'
                    }
                ),
                style={
                    'height': '100%',
                    'width': '100%',
                    'backgroundColor': 'darkgreen',
                    'borderRadius': '10px'
                }
            ),
            id='hover',
            style={
                'margin': '0 auto',
                'height': '300px',
                'width': '300px'
            }
        ),
        html.Pre(id='output'),
    ],
    style={
        'padding': 50
    }
)


@app.callback(
    Output('output', 'children'),
    [Input('hover', 'listenMove'),
     Input('hover', 'listenEnter'),
     Input('hover', 'listenLeave')]
)
def display_output(listenMove, listenEnter, listenLeave):
    return json.dumps(
        {
            'listenMove': listenMove,
            'listenEnter': listenEnter,
            'listenLeave': listenLeave
        },
        indent=2
    )


if __name__ == '__main__':
    app.run_server(debug=True)
