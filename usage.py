import dash
from dash import html
import feffery_utils_components as fuc
from dash.dependencies import Input, Output

app = dash.Dash(__name__)

app.layout = html.Div(
    [
        html.Button(
            '还原favicon',
            id='clear-demo-output'
        ),
        html.Div(
            fuc.FefferySetFavicon(
                favicon='https://www.google.com/favicon.ico'
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

    return fuc.FefferySetFavicon(
        favicon='/_favicon.ico'
    )


if __name__ == '__main__':
    app.run(debug=True)
