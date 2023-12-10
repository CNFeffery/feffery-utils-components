import dash
from dash import html
import feffery_utils_components as fuc
from dash.dependencies import Input, Output, State

app = dash.Dash(__name__, compress=True)

app.layout = html.Div(
    [
        fuc.FefferyAutoFit(
            id='auto-fit',
            containerId='app-container'
        ),
        html.Div(
            id='div-demo1',
            style={
                'height': '500px',
                'width': '500px',
                'background': 'grey',
                'borderRadius': '8px',
                'color': 'white',
                'margin': '10px',
                'float': 'left'
            }
        ),
        html.Div(
            id='div-demo2',
            style={
                'height': '500px',
                'width': '500px',
                'background': 'grey',
                'borderRadius': '8px',
                'color': 'white',
                'margin': '10px',
                'float': 'left'
            }
        ),
        html.Div(
            id='div-demo3',
            style={
                'height': '500px',
                'width': '500px',
                'background': 'grey',
                'borderRadius': '8px',
                'color': 'white',
                'margin': '10px',
                'float': 'left'
            }
        ),
    ],
    id='app-container'
)


if __name__ == '__main__':
    app.run_server(debug=True)
