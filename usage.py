import dash
from dash import html
import feffery_utils_components as fuc
from dash.dependencies import Input, Output, State

app = dash.Dash(__name__, compress=True)

app.layout = html.Div(
    [
        fuc.FefferyVirtualList(
            id='virtual-list-demo',
            height=400,
            itemHeight=40,
            children=[html.Div(i) for i in range(1000)]
        )
    ],
    style={
        'padding': 25
    }
)


if __name__ == '__main__':
    app.run_server(debug=True)
