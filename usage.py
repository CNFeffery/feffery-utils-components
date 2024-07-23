import dash
import json
from dash import html
import feffery_utils_components as fuc
from dash.dependencies import Input, Output

app = dash.Dash(__name__)

app.layout = html.Div(
    [
        html.Div(
            [
                html.Div(
                    id='drag-block-demo',
                    style={
                        'width': 100,
                        'height': 100,
                        'border': '1px solid black',
                        'cursor': 'move',
                    },
                )
            ],
            style={'padding': 24},
        ),
        html.Div(
            id='drop-container-demo',
            style={
                'height': 500,
                'border': '1px solid red',
            },
        ),
        fuc.FefferyListenDrag(
            targetSelector='#drag-block-demo', data='测试'
        ),
        fuc.FefferyListenDrop(
            id='listen-drop-demo',
            targetSelector='#drop-container-demo',
        ),
    ],
    style={'padding': 50},
)


@app.callback(
    Output('drop-container-demo', 'children'),
    Input('listen-drop-demo', 'dropEvent'),
    prevent_initial_call=True,
)
def listen_drop_event(dropEvent):
    return json.dumps(
        dropEvent, indent=4, ensure_ascii=False
    )


if __name__ == '__main__':
    app.run(debug=True)
