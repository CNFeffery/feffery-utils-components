import json
import dash
from dash import html
import feffery_utils_components as fuc
from dash.dependencies import Input, Output

app = dash.Dash(__name__)

app.layout = html.Div(
    [
        html.Button(
            '点我',
            id='button-demo'
        ),
        fuc.FefferyDebounceProp(
            id='debounce-prop-demo',
            debounceWait=500
        ),
        html.Pre(
            id='output'
        )
    ],
    style={
        'padding': 50
    }
)


app.clientside_callback(
    '''(n_clicks) => n_clicks''',
    Output('debounce-prop-demo', 'sourceProp'),
    Input('button-demo', 'n_clicks'),
    prevent_initial_call=True
)


@app.callback(
    Output('output', 'children'),
    Input('debounce-prop-demo', 'debounceProp'),
    prevent_initial_call=True
)
def update_output(debounceProp):

    return json.dumps(
        dict(n_clicks=debounceProp),
        indent=4,
        ensure_ascii=False
    )


if __name__ == '__main__':
    app.run(debug=True)
