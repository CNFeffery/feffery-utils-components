import dash
import json
from dash import html
import feffery_utils_components as fuc
from dash.dependencies import Input, Output

app = dash.Dash(__name__)

app.layout = html.Div(
    [
        html.Button(
            '传送！',
            id='render-portal'
        ),
        html.Div(
            id='portal-container'
        ),
        html.Div(
            html.Div(
                html.Div(
                    html.Div(
                        html.Div(
                            html.Div(
                                id='portal-target'
                            )
                        )
                    )
                )
            ),
            style={
                'position': 'fixed',
                'background': 'white',
                'border': '1px solid black',
                'top': 24,
                'right': 24,
                'padding': 24
            }
        )
    ],
    style={
        'padding': '300px 100px'
    }
)


@app.callback(
    Output('portal-container', 'children'),
    Input('render-portal', 'n_clicks'),
    prevent_initial_call=True
)
def render_portal(n_clicks):

    return fuc.FefferyPortal(
        html.Div(
            '传送内容',
            id='portal-demo'
        ),
        targetSelector='#portal-target'
    )

if __name__ == '__main__':
    app.run(debug=True)
