import dash
import json
from dash import html
import feffery_utils_components as fuc
from dash.dependencies import Input, Output, State

app = dash.Dash(__name__)

app.layout = html.Div(
    [
        fuc.FefferyDiv(
            id='div-demo',
            style={
                'minHeight': 300,
                'background': '#d9d9d9',
                'padding': 12
            }
        ),
        # fuc.FefferyDebugGuardian(
        #     strategy='debugger-then-execute-js',
        #     # jsString='alert("禁止调试")',
        #     jsString='document.write('')'
        # )
    ],
    style={
        'padding': '50px 50px 0 50px'
    }
)


@app.callback(
    Output('div-demo', 'children'),
    [Input('div-demo', 'clickEvent'),
     Input('div-demo', 'doubleClickEvent')],
    prevent_initial_call=True
)
def demo(clickEvent, doubleClickEvent):

    return html.Pre(
        json.dumps(
            dict(
                clickEvent=clickEvent,
                doubleClickEvent=doubleClickEvent
            ),
            indent=4,
            ensure_ascii=False
        )
    )


if __name__ == '__main__':
    app.run(debug=True)
