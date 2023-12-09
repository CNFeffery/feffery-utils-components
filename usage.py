
import dash
from dash import html
import feffery_utils_components as fuc
from dash.dependencies import Input, Output
import uuid

app = dash.Dash(__name__, compress=True)

app.layout = html.Div(
    [

        html.Div(
            [
                html.Div(
                    style={
                        'height': '800px'
                    }
                ),
                fuc.FefferyLazyLoad(
                    html.Div(
                        html.Img(
                            src='https://fac.feffery.tech/assets/imgs/fac-logo.svg?token=' +
                            str(uuid.uuid4()),
                            style={
                                'height': '100%'
                            }
                        ),
                        style={
                            'height': '100px',
                            'border': '1px dashed #c8c6c4'
                        }
                    ),
                    height=100
                )
            ],
            style={
                'maxHeight': '300px',
                'overflow': 'auto'
            }
        )
    ],
    style={
        'padding': 25
    }
)


if __name__ == '__main__':
    app.run_server(debug=True)
