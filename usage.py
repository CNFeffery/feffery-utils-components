import dash
import json
from dash import html, dcc
import feffery_utils_components as fuc
from dash.dependencies import Input, Output

app = dash.Dash(__name__)

app.layout = html.Div(
    [
        html.Button(
            '销毁',
            id='clear-demo-output'
        ),
        html.Div(
            fuc.FefferySetTitle(
                title='测试title',
                originTitle='默认title'
            ),
            id='demo-output'
        )
    ],
    style={
        'padding': '50px 50px 0 50px'
    }
)


@app.callback(
    Output('demo-output', 'children'),
    Input('clear-demo-output', 'n_clicks'),
    prevent_initial_call=True
)
def demo(n_clicks):

    return


if __name__ == '__main__':
    app.run(debug=True)
