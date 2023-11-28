import dash
from dash import html
import feffery_utils_components as fuc
from dash.dependencies import Input, Output, State

app = dash.Dash(__name__)

app.layout = html.Div(
    [
        fuc.FefferyFancyButton(
            '测试',
            id='trigger'
        ),
        fuc.FefferyThrottleProp(
            id='demo-throttle-prop',
            throttleWait=1000
        ),
        html.Pre(id='output')
    ],
    style={
        'padding': 50
    }
)

app.clientside_callback(
    '''(nClicks) => nClicks''',
    Output('demo-throttle-prop', 'sourceProp'),
    Input('trigger', 'nClicks'),
    prevent_initial_call=True
)


@app.callback(
    Output('output', 'children'),
    Input('demo-throttle-prop', 'throttleProp'),
    prevent_initial_call=True
)
def update_throttle_prop(throttleProp):

    return f'throttleProp: {throttleProp}'


if __name__ == '__main__':
    app.run(debug=True)
