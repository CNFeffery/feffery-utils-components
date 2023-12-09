
import dash
from dash import html
import feffery_utils_components as fuc
from dash.dependencies import Input, Output
import uuid

app = dash.Dash(__name__, compress=True)

app.layout = html.Div(
    [
        fuc.FefferyScrollbars(
            html.Div(
                '请将鼠标移入本区域进行滚动\n'*100,
                style={
                    'whiteSpace': 'pre'
                }
            ),
            style={
                'maxHeight': '150px',
                'maxWidth': '200px',
                'border': '1px dashed #e1dfdd'
            }
        )
    ],
    style={
        'padding': 25
    }
)


if __name__ == '__main__':
    app.run_server(debug=True)
