import dash
from dash import html
import feffery_utils_components as fuc
from dash.dependencies import Input, Output, State

app = dash.Dash(
    __name__,
    suppress_callback_exceptions=True
)

app.layout = html.Div(
    [
        fuc.FefferyListenUnload(
            id='listen-unload'
        ),
        html.Div(
            id='output-demo'
        )
    ],
    style={
        'padding': '50px 100px'
    }
)


@app.callback(
    Output('output-demo', 'children'),
    Input('listen-unload', 'unloaded')
)
def demo(unloaded):

    if unloaded:

        print('页面被关闭')


if __name__ == '__main__':
    app.run(debug=True)
