import json
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
        fuc.FefferyDiv(
            id='input',
            shadow='always-shadow',
            style={
                'width': 500,
                'height': 300
            }
        ),
        html.Div(
            id='output'
        )
    ],
    style={
        'padding': '50px 100px',
        'height': 99999,
        'width': 99999
    }
)


app.clientside_callback(
    '''( pasteCount, pasteText ) => `${pasteText} ${pasteCount}`''',
    Output('output', 'children'),
    Input('input', 'pasteCount'),
    State('input', 'pasteText'),
    prevent_initial_call=True
)


if __name__ == '__main__':
    app.run(debug=True)
