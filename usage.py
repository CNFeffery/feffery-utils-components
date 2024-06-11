import dash
import json
from dash import html
import feffery_utils_components as fuc
from dash.dependencies import Input, Output

app = dash.Dash(__name__)

app.layout = html.Div(
    [
        html.Button('示例按钮', id='target-demo'),
        fuc.FefferyEventListener(
            id='event-listener-demo',
            eventName='click',
            handler="""(e) => {
                console.log(e)
                return {
                    result: {
                        event: eventName,
                        timestamp: Date.now()
                    }
                };
            }""",
            targetSelector='#target-demo',
        ),
        html.Pre(id='result'),
    ],
    style={'padding': 50},
)


@app.callback(
    Output('result', 'children'),
    Input('event-listener-demo', 'result'),
    prevent_initial_call=True,
)
def show_result(result):
    return json.dumps(result, indent=4, ensure_ascii=False)


if __name__ == '__main__':
    app.run(debug=True)
