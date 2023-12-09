
import dash
from dash import html
import feffery_utils_components as fuc
from dash.dependencies import Input, Output
import uuid

app = dash.Dash(__name__, compress=True)

app.layout = html.Div(
    [
        html.Div(
            style={
                'height': '200px'
            }
        ),
        fuc.FefferySticky(
            html.Div(
                '请向下滚动查看效果',
                style={
                    'backgroundColor': 'green'
                }
            ),
            top=25,
            bottomBoundary=800
        ),
        html.Div(
            style={
                'height': '1200px'
            }
        )
    ],
    style={
        'padding': 25
    }
)


if __name__ == '__main__':
    app.run_server(debug=True)
