import dash
from dash import html
import feffery_utils_components as fuc
from dash.dependencies import Input, Output, State

app = dash.Dash(__name__)

app.layout = html.Div(
    [
        fuc.FefferyDiv(
            id='paste-target-container',
            shadow='always-shadow',
            style={
                'width': 500,
                'height': 300
            }
        ),
        fuc.FefferyListenPaste(
            id='listen-paste',
            # enableListenPaste=True,
            targetContainerId='paste-target-container'
        )
    ],
    style={
        'padding': '50px 100px'
    }
)


@app.callback(
    Output('paste-target-container', 'children'),
    Input('listen-paste', 'pasteCount'),
    State('listen-paste', 'pasteText'),
    prevent_initial_call=True
)
def demo(pasteCount, pasteText):

    return f'pasteCount: {pasteCount}  pasteText: {pasteText}'


if __name__ == '__main__':
    app.run(debug=True)
